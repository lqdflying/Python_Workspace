# -*- coding:utf-8 -*-
###
# File: gen_Inventory.py
# Created Date: 2020-06-17
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Saturday June 20th 2020 11:55:00 am
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###


import atexit
import datetime
import itertools
import json
import os
import re
import ssl
import sys
import uuid
import pprint
from time import time

from jinja2 import Environment

import configparser

try:
    import argparse
except ImportError:
    sys.exit('Error: This inventory script required "argparse" python module.  Please install it or upgrade to python-2.7')

try:
    from pyVmomi import vim, vmodl
    from pyVim.connect import SmartConnect, Disconnect
except ImportError:
    sys.exit("ERROR: This inventory script required 'pyVmomi' Python module, it was not able to load it")


def regex_match(s, pattern):
    '''Custom filter for regex matching'''
    reg = re.compile(pattern)
    if reg.match(s):
        return True
    else:
        return False
class genInventory(object):
    __name__ = 'genInventory'
    guest_props = False
    instances = []
    debug = False
    load_dumpfile = None
    write_dumpfile = None
    maxlevel = 1
    lowerkeys = True
    config = None
    cache_max_age = None
    cache_path_cache = None
    cache_path_index = None
    cache_dir = None
    server = None
    port = None
    username = None
    password = None
    validate_certs = True
    host_filters = []
    skip_keys = []
    groupby_patterns = []
    groupby_custom_field_excludes = []

    safe_types = [bool, str, float, None]
    iter_types = [dict, list]

    bad_types = ['Array', 'disabledMethod', 'declaredAlarmState']

    vimTableMaxDepth = {
        "vim.HostSystem": 2,
        "vim.VirtualMachine": 2,
    }


    vimTable = {
        vim.Datastore: ['_moId', 'name'],
        vim.ResourcePool: ['_moId', 'name'],
        vim.HostSystem: ['_moId', 'name'],
    }

    def __init__(self):
        self.read_settings()
        # self.inventory = self.get_instances()
        # self.inventory = self.get_inventory_from_cache()
    def debugl(self, text):
        try:
            text = str(text)
        except UnicodeEncodeError:
            text = text.encode('utf-8')
        print('%s %s' % (datetime.datetime.now(), text))

    def read_settings(self):
        ''' Reads the settings from the vmware_inventory.ini file '''

        scriptbasename = __file__
        scriptbasename = os.path.basename(scriptbasename)
        scriptbasename = scriptbasename.replace('.py', '')

        defaults = {'vmware': {
            'server': '',
            'port': 443,
            'username': '',
            'password': '',
            'validate_certs': False,
            'ini_path': os.path.join(os.path.dirname(__file__), '%s.ini' % scriptbasename),
            'cache_name': 'ansible-vmware',
            'cache_path': '~/.ansible/tmp',
            'cache_max_age': 3600,
            'max_object_level': 1,
            'skip_keys': 'declaredalarmstate,'
                         'disabledmethod,'
                         'dynamicproperty,'
                         'dynamictype,'
                         'environmentbrowser,'
                         'managedby,'
                         'parent,'
                         'childtype,'
                         'resourceconfig',
            'alias_pattern': '{{ config.name + "_" + config.uuid }}',
            'host_pattern': '{{ guest.ipaddress }}',
            'host_filters': '{{ runtime.powerstate == "poweredOn" }}',
            'groupby_patterns': '{{ guest.guestid }},{{ "templates" if config.template else "guests"}}',
            'lower_var_keys': True,
            'custom_field_group_prefix': 'vmware_tag_',
            'groupby_custom_field_excludes': '',
            'groupby_custom_field': False
            }
        }
        
        config = configparser.ConfigParser()
        # where is the config?
        vmware_ini_path = os.environ.get('VMWARE_INI_PATH', defaults['vmware']['ini_path'])
        # vmware_ini_path = os.path.expanduser(os.path.expandvars(vmware_ini_path)) #不在用户home目录下放配置文件
        config.read(vmware_ini_path)

        if 'vmware' not in config.sections():
            config.add_section('vmware')

        # apply defaults
        for k, v in defaults['vmware'].items():
            if not config.has_option('vmware', k):
                config.set('vmware', k, str(v))

        # mark the connection info
        self.server = os.environ.get('VMWARE_SERVER', config.get('vmware', 'server'))
        self.debugl('server is %s' % self.server)
        self.port = int(os.environ.get('VMWARE_PORT', config.get('vmware', 'port')))
        self.username = os.environ.get('VMWARE_USERNAME', config.get('vmware', 'username'))
        self.debugl('username is %s' % self.username)
        self.password = os.environ.get('VMWARE_PASSWORD', config.get('vmware', 'password', raw=True))
        self.validate_certs = os.environ.get('VMWARE_VALIDATE_CERTS', config.get('vmware', 'validate_certs'))
        if self.validate_certs in ['no', 'false', 'False', False]:
            self.validate_certs = False

        self.debugl('cert validation is %s' % self.validate_certs)

        # behavior control
        self.maxlevel = int(config.get('vmware', 'max_object_level'))
        self.debugl('max object level is %s' % self.maxlevel)
        self.lowerkeys = config.get('vmware', 'lower_var_keys')
        if type(self.lowerkeys) != bool:
            if str(self.lowerkeys).lower() in ['yes', 'true', '1']:
                self.lowerkeys = True
            else:
                self.lowerkeys = False
        self.debugl('lower keys is %s' % self.lowerkeys)
        self.skip_keys = list(config.get('vmware', 'skip_keys').split(','))
        self.debugl('skip keys is %s' % self.skip_keys)
        if config.has_section('properties'):
            self.guest_props = []
            for prop in config.items('properties'):
                self.guest_props.append(prop[1])
        self.config = config

    def get_Section(self):
        '''所有的配置信息'''
        for i in self.config.sections():
            print(self.config.items(i))
        '''自定义属性信息'''
        print(self.guest_props)

    def get_instances(self):
        ''' Get a list of vm instances with pyvmomi '''
        kwargs = {'host': self.server,
                  'user': self.username,
                  'pwd': self.password,
                  'port': int(self.port)}

        if self.validate_certs and hasattr(ssl, 'SSLContext'):
            context = ssl.SSLContext(ssl.PROTOCOL_TLS)
            context.verify_mode = ssl.CERT_REQUIRED
            context.check_hostname = True
            kwargs['sslContext'] = context
        elif self.validate_certs and not hasattr(ssl, 'SSLContext'):
            sys.exit('pyVim does not support changing verification mode with python < 2.7.9. Either update '
                     'python or use validate_certs=false.')
        elif not self.validate_certs and hasattr(ssl, 'SSLContext'):
            context = ssl.SSLContext(ssl.PROTOCOL_TLS)
            context.verify_mode = ssl.CERT_NONE
            context.check_hostname = False
            kwargs['sslContext'] = context #为kwargs这个dict附加了一个'sslContext'的key,value是按照参数要求设置好的SSL 上下文
        elif not self.validate_certs and not hasattr(ssl, 'SSLContext'):
            # Python 2.7.9 < or RHEL/CentOS 7.4 <
            pass

        return self._get_instances(kwargs)

    def get_method(self,vobj):
        methods = dir(vobj)
        methods = [str(x) for x in methods if not x.startswith('_')]
        methods = [x for x in methods if x not in self.bad_types]
        methods = [x for x in methods if not x.lower() in self.skip_keys]
        methods = sorted(methods)
        return methods
        # print("method:\n",methods) #all the method a vm object have

    def get_subclass(self,vobj):
        if vobj is None:
            return 'None'
        elif type(vobj) in self.vimTable:
            return 'self.vimTable'
        elif issubclass(type(vobj), str) or isinstance(vobj, str):
            return 'str'
        elif issubclass(type(vobj), bool) or isinstance(vobj, bool):
            return 'bool'
        elif issubclass(type(vobj), float) or isinstance(vobj, float):
            return 'float'
        elif issubclass(type(vobj), list) or issubclass(type(vobj), tuple):
            return 'list'
        elif issubclass(type(vobj), dict):
            return 'dict'
        elif issubclass(type(vobj), object):
            return 'object'
        else:
            return 'final'

    def _get_instances(self, inkwargs):
        ''' 
        Make API calls
        def SmartConnect(protocol='https', host='localhost', port=443, user='root', pwd='',
                service="hostd", path="/sdk", connectionPoolTimeout=CONNECTION_POOL_IDLE_TIMEOUT_SEC,
                preferredApiVersions=None, keyFile=None, certFile=None,
                thumbprint=None, sslContext=None, b64token=None, mechanism='userpass'):
            <...>
        '''
        instances = []
        try:
            si = SmartConnect(**inkwargs) 
        except ssl.SSLError as connection_error:
            if '[SSL: CERTIFICATE_VERIFY_FAILED]' in str(connection_error) and self.validate_certs:
                sys.exit("Unable to connect to ESXi server due to %s, "
                         "please specify validate_certs=False and try again" % connection_error)

        except Exception as exc:
            self.debugl("Unable to connect to ESXi server due to %s" % exc)
            sys.exit("Unable to connect to ESXi server due to %s" % exc)

        self.debugl('retrieving all instances')
        if not si:
            sys.exit("Could not connect to the specified host using specified "
                     "username and password")
        atexit.register(Disconnect, si)
        content = si.RetrieveContent()
        print('type(content):',type(content)) #<class 'pyVmomi.VmomiSupport.vim.ServiceInstanceContent'>
        print('content.rootFolder:', content.rootFolder)
        container = content.rootFolder
        viewType = [vim.VirtualMachine]
        recursive = True
        containerView = content.viewManager.CreateContainerView(container, viewType, recursive)
        print('containerView.view:', containerView.view)
        for child in containerView.view: instances.append(child)
        print('instances:', instances)
        cfm = content.customFieldsManager
        print('content.customFieldsManager:', cfm)

        print("vm对象可用方法集合:\n",self.get_method(instances[0]))
        
        instance_dict = {}
        for instance in instances:
            # ifacts = self.facts_from_vobj(instance)
            ifacts = self.facts_from_proplist(instance)
            instance_dict[instance] = ifacts
        print(type(instance_dict))
        pprint.pprint(instance_dict)
        
        '''
        print("type(instances[0]):---->",type(instances[0]))
        print("get_subclass(instances[0]):---->",self.get_subclass(instances[0]))
        #<class 'pyVmomi.VmomiSupport.vim.VirtualMachine'>
        

        a = getattr(instances[0], 'config')
        b = getattr(instances[0], 'datastore')
        print("type(a),打印a的类型:") #<class 'pyVmomi.VmomiSupport.vim.vm.ConfigInfo'>
        print(type(a))
        print("type(a).__name__,打印a的名字:") #<class 'pyVmomi.VmomiSupport.vim.vm.ConfigInfo'>
        print(type(a).__name__)   #vim.vm.ConfigInfo   
        print("get_subclass(a),判断a属于哪一类子类:") 
        print(self.get_subclass(a))   #object


        print("type(b),打印b的类型:") #<class 'pyVmomi.VmomiSupport.vim.vm.ConfigInfo'>
        print(type(b))
        print("type(b).__name__,打印b的名字:") #<class 'pyVmomi.VmomiSupport.vim.vm.ConfigInfo'>
        print(type(b).__name__)   #vim.vm.ConfigInfo  
        print("get_subclass(b),判断b属于哪一类子类:") 
        print(self.get_subclass(b))   #list
        for i in b:
            print(type(i)) #<class 'pyVmomi.VmomiSupport.vim.Datastore'>
            print(self.get_subclass(i)) #self.vimTable
        # print("getattr(instances[0], config)的输出:")
        # pprint.pprint(b._moId)
        '''


    def facts_from_proplist(self, vm):
        '''Get specific properties instead of serializing everything'''

        rdata = {}
        for prop in self.guest_props:
            self.debugl('getting %s property for %s' % (prop, vm.name))
            key = prop
            if self.lowerkeys:
                key = key.lower()

            if '.' not in prop:
                # props without periods are direct attributes of the parent
                try:
                    methodToCall = getattr(vm, prop)
                except Exception as e:
                    continue
                
                # Skip callable methods
                if callable(methodToCall):
                    continue
                
                if self.lowerkeys:
                    prop = prop.lower()
    
                rdata[prop] = self._process_object_types(
                    methodToCall,
                    thisvm=vm
                )
                '''
                vm_property = getattr(vm, prop)
                if isinstance(vm_property, vim.CustomFieldsManager.Value.Array):
                    temp_vm_property = []
                    for vm_prop in vm_property:
                        temp_vm_property.append({'key': vm_prop.key,
                                                 'value': vm_prop.value})
                    rdata[key] = temp_vm_property
                else:
                    rdata[key] = vm_property
                '''    
            else:
                # props with periods are subkeys of parent attributes
                parts = prop.split('.')
                total = len(parts) - 1 #len(parts) = 2

                # pointer to the current object
                val = None
                # pointer to the current result key
                lastref = rdata

                for idx, x in enumerate(parts): #[(0, config),(1, cpuHotAddEnabled)]

                    if isinstance(val, dict): 
                        if x in val:
                            val = val.get(x)
                        elif x.lower() in val:
                            val = val.get(x.lower())
                    else:
                        # if the val wasn't set yet, get it from the parent
                        if not val:
                            try:
                                val = getattr(vm, x) #val = getattr(vm, config), see tmp_file/raw_vim.vm.ConfigInfo.txt
                            except AttributeError as e:
                                self.debugl(e)
                        else:
                            # in a subkey, get the subprop from the previous attrib
                            try:
                                val = getattr(val, x)
                            except AttributeError as e:
                                self.debugl(e)

                        # make sure it serializes
                        val = self._process_object_types(val) # self._process_object_types(val)这里传入的是tmp_file/raw_vim.vm.ConfigInfo.txt的内容

                    # lowercase keys if requested
                    if self.lowerkeys:
                        x = x.lower() #for the first time,x is 'config'

                    # change the pointer or set the final value
                    if idx != total: #for the first run, idx = 0
                        if x not in lastref:   #for the first run, lastref = {}
                            lastref[x] = {}    #lastref[config] = {}
                        lastref = lastref[x]   #lastref = lastref[config]
                    else:
                        lastref[x] = val
        # self.debugl("For %s" % vm.name)
        # for key in list(rdata.keys()):
        #     if isinstance(rdata[key], dict):
        #         for ikey in list(rdata[key].keys()):
        #             self.debugl("Property '%s.%s' has value '%s'" % (key, ikey, rdata[key][ikey]))
        #     else:
        #         self.debugl("Property '%s' has value '%s'" % (key, rdata[key]))
        return rdata

    def facts_from_vobj(self, vobj, level=0):
        ''' Traverse a VM object and return a json compliant data structure '''

        # pyvmomi objects are not yet serializable, but may be one day ...
        # https://github.com/vmware/pyvmomi/issues/21

        # WARNING:
        # Accessing an object attribute will trigger a SOAP call to the remote.
        # Increasing the attributes collected or the depth of recursion greatly
        # increases runtime duration and potentially memory+network utilization.
        
        if level == 0:
            try:
                self.debugl("get facts for %s" % vobj.name)
            except Exception as e:
                self.debugl(e)

        rdata = {}

        methods = dir(vobj)
        methods = [str(x) for x in methods if not x.startswith('_')]
        methods = [x for x in methods if x not in self.bad_types]
        methods = [x for x in methods if not x.lower() in self.skip_keys]
        methods = sorted(methods)

        for method in methods:
            # Attempt to get the method, skip on fail
            try:
                methodToCall = getattr(vobj, method)
            except Exception as e:
                continue

            # Skip callable methods
            if callable(methodToCall):
                continue

            if self.lowerkeys:
                method = method.lower()

            rdata[method] = self._process_object_types(
                methodToCall,
                thisvm=vobj,
                inkey=method,
            )

        return rdata

    def _process_object_types(self, vobj, thisvm=None, inkey='', level=0):
        ''' Serialize an object '''
        rdata = {}
        #for the first run: type(vobj).__name__ = vim.vm.ConfigInfo
        if type(vobj).__name__ in self.vimTableMaxDepth and level >= self.vimTableMaxDepth[type(vobj).__name__]: 
            return rdata        
        '''
        #self.vimTableMaxDepth[type(vobj).__name__] = 2 ,所以这里的条件永远不成立
        
        vimTableMaxDepth = {
            "vim.HostSystem": 2,
            "vim.VirtualMachine": 2,
        }
        '''

        if vobj is None:
            rdata = None
        elif type(vobj) in self.vimTable:
            '''
            vimTable = {
                vim.Datastore: ['_moId', 'name'],
                vim.ResourcePool: ['_moId', 'name'],
                vim.HostSystem: ['_moId', 'name'],
            }
            '''
            rdata = {}
            for key in self.vimTable[type(vobj)]:
                try:
                    rdata[key] = getattr(vobj, key)
                except Exception as e:
                    self.debugl(e)

        elif issubclass(type(vobj), str) or isinstance(vobj, str):
            if vobj.isalnum():
                rdata = vobj
            else:
                rdata = vobj.encode('utf-8').decode('utf-8')
        elif issubclass(type(vobj), bool) or isinstance(vobj, bool):
            rdata = vobj
        # elif issubclass(type(vobj), integer_types) or isinstance(vobj, integer_types):
        #     rdata = vobj
        elif issubclass(type(vobj), float) or isinstance(vobj, float):
            rdata = vobj
        elif issubclass(type(vobj), list) or issubclass(type(vobj), tuple):
            rdata = []
            try:
                vobj = sorted(vobj)
            except Exception:
                pass

            for idv, vii in enumerate(vobj):
                if level + 1 <= self.maxlevel:
                    vid = self._process_object_types(
                        vii,
                        thisvm=thisvm,
                        inkey=inkey + '[' + str(idv) + ']',
                        level=(level + 1)
                    )

                    if vid:
                        rdata.append(vid)

        elif issubclass(type(vobj), dict):
            pass

        elif issubclass(type(vobj), object):
            methods = dir(vobj)
            methods = [str(x) for x in methods if not x.startswith('_')]
            methods = [x for x in methods if x not in self.bad_types]
            methods = [x for x in methods if not inkey + '.' + x.lower() in self.skip_keys]
            methods = sorted(methods)

            for method in methods:
                # Attempt to get the method, skip on fail
                try:
                    methodToCall = getattr(vobj, method)
                except Exception as e:
                    continue

                if callable(methodToCall):
                    continue

                if self.lowerkeys:
                    method = method.lower()
                if level + 1 <= self.maxlevel:
                    try:
                        rdata[method] = self._process_object_types(
                            methodToCall,
                            thisvm=thisvm,
                            inkey=inkey + '.' + method,
                            level=(level + 1)
                        )
                    except vim.fault.NoPermission:
                        self.debugl("Skipping method %s (NoPermission)" % method)
        else:
            pass

        return rdata


if __name__ == "__main__":
    vcsa = genInventory()
    vcsa.get_instances()
    # vcsa.get_Section()