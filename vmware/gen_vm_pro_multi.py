# -*- coding:utf-8 -*-
###
# File: gen_vm_pro_multi_test.py
# Created Date: 2020-06-22
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Wednesday June 24th 2020 4:55:55 pm
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
from multiprocessing import Pool

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
validIpAddressRegex = "^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
nbuNetWork = "^(?:9\\.7\\.65\\.)(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
validNetWork = "^(?:9\\.)(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){2}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

class genConfig(object):
    __name__ = 'genConfig'
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
        self.gen_vim_vars()
        
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

    def gen_vim_vars(self):
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
        self.kwargs = kwargs


class genClusterNum(genConfig):
    def __init__(self):
        super(genClusterNum,self).__init__()
        
    def get_Cluster_num(self):
        ''' Get a list of vm instances with pyvmomi '''
        try:
            si = SmartConnect(**self.kwargs) 
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
        cluster_num = len(content.rootFolder.childEntity[0].hostFolder.childEntity)
        return cluster_num

class genFacts(genConfig):
    def __init__(self,cluster_id):
        super(genFacts,self).__init__()
        self.cluster_id = cluster_id
        
    def facts_from_proplist(self, n, vm):
        '''Get specific properties instead of serializing everything'''

        rdata = {}
        for prop in self.guest_props:
            self.debugl('Process ID[%s] : getting %s property for %s' % (n, prop, vm.name))
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
            else:
                # props with periods are subkeys of parent attributes
                parts = prop.split('.')
                total = len(parts) - 1 #len(parts) = 2, so total = 1

                # pointer to the current object
                val = {}
                
                # pointer to the current result key
                lastref = rdata

                for idx, x in enumerate(parts): 

                    if isinstance(val, dict) and len(val) != 0: 
                        if x in val:
                            val = val.get(x)
                        elif x.lower() in val:
                            val = val.get(x.lower())
                    else:
                        # if the val wasn't set yet, get it from the parent
                        if not val:
                            try:
                                val = getattr(vm, x) 
                            except AttributeError as e:
                                self.debugl(e)
                        else:
                            # in a subkey, get the subprop from the previous attrib
                            try:
                                val = getattr(val, x)
                            except AttributeError as e:
                                self.debugl(e)

                        # make sure it serializes
                        # val = self._process_object_types(val)
                        val = self._process_object_types(
                            val,
                            thisvm=vm
                        )
                    # lowercase keys if requested
                    if self.lowerkeys:
                        x = x.lower() 

                    # change the pointer or set the final value
                    if idx != total: 
                        if x not in lastref:   
                            lastref[x] = {}    
                        lastref = lastref[x]   
                    else:
                        lastref[x] = val
                        
        return rdata

    def _process_object_types(self, vobj, thisvm=None, inkey='', level=0):
        ''' Serialize an object '''
        rdata = {}
        #for the first run: type(vobj).__name__ = vim.vm.ConfigInfo
        if type(vobj).__name__ in self.vimTableMaxDepth and level >= self.vimTableMaxDepth[type(vobj).__name__]: 
            return rdata

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
            elif regex_match(vobj, validIpAddressRegex): #ip address: 9.7.65.33 gw:9.7.68.254
                if not regex_match(vobj, nbuNetWork) and regex_match(vobj, validNetWork):
                    rdata = vobj
                elif regex_match(vobj, nbuNetWork):
                    gw = []
                    for i in thisvm.guest.ipStack[0].ipRouteConfig.ipRoute: gw.append(i.gateway.ipAddress)
                    if regex_match(list(filter(None, gw))[0], nbuNetWork):
                        rdata = vobj
                else:
                    for i in thisvm.guest.net:
                        for m in i.ipAddress:
                            if regex_match(m, validNetWork):
                                rdata = m
                                break
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

    def get_facts_subprocessing(self):
        inventorys = {}
        self.debugl("进程{}开始执行".format(self.cluster_id))
        try:
            si = SmartConnect(**self.kwargs) 
        except ssl.SSLError as connection_error:
            if '[SSL: CERTIFICATE_VERIFY_FAILED]' in str(connection_error) and self.validate_certs:
                sys.exit("Unable to connect to ESXi server due to %s, "
                         "please specify validate_certs=False and try again" % connection_error)

        except Exception as exc:
            self.debugl("Unable to connect to ESXi server due to %s" % exc)
            sys.exit("Unable to connect to ESXi server due to %s" % exc)

        self.debugl('Cluster_id[%s]: retrieving all instances'%(self.cluster_id))
        if not si:
            sys.exit("Could not connect to the specified host using specified "
                     "username and password")
        atexit.register(Disconnect, si)
        content = si.RetrieveContent()
        viewType = [vim.VirtualMachine]
        recursive = True
        cluster_obj = content.rootFolder.childEntity[0].hostFolder.childEntity[self.cluster_id]
        inventorys[cluster_obj.name] = {}
        # inventorys[cluster_obj.name]['name'] = cluster_obj.name
        containerView = content.viewManager.CreateContainerView(cluster_obj, viewType, recursive)
        for vm in containerView.view: 
            ifacts = self.facts_from_proplist(self.cluster_id, vm)
            inventorys[cluster_obj.name][vm] = ifacts
        return inventorys

def get_Cluster_facts(id):
    get_Cluster_facts = genFacts(id)
    result =  get_Cluster_facts.get_facts_subprocessing()
    # return type(result)
    return str(result)
    # print(type(result))
    # pprint.pprint(result)

def combine_Data(var):
    # pprint.pprint(eval(var))
    final_facts.update(eval(var))

def main():
    vcsa_num = genClusterNum().get_Cluster_num()
    p = Pool(processes=vcsa_num)

    # inventory_facts = ""
    for i in range(vcsa_num):
        p.apply_async(get_Cluster_facts, args=(i,), callback=combine_Data)
        # pprint.pprint(result)
    p.close()
    p.join()
    # pprint.pprint(inventory_facts)

result = {'SDK_TEST': {'name': 'SDK_TEST',
              'vim.VirtualMachine:vm-17': {'config': {'name': 'vcsa_dev_7.68.210',
                                                      'template': False},
                                           'datastore': [{'_moId': 'datastore-11',
                                                          'name': '68.25_Local'}],
                                           'guest': {'guestid': 'sles11_64Guest',
                                                     'gueststate': 'running',
                                                     'hostname': 'localhost.localdom',
                                                     'ipaddress': '9.7.68.210'},
                                           'name': 'vcsa_dev_7.68.210'},
              'vim.VirtualMachine:vm-18': {'config': {'name': 'RHEL7.5_Temp',
                                                      'template': True},
                                           'datastore': [{'_moId': 'datastore-11',
                                                          'name': '68.25_Local'}],
                                           'guest': {'guestid': None,
                                                     'gueststate': 'notRunning',
                                                     'hostname': None,
                                                     'ipaddress': None},
                                           'name': 'RHEL7.5_Temp'},
              'vim.VirtualMachine:vm-19': {'config': {'name': 'Winserver2008R2_TMP',
                                                      'template': True},
                                           'datastore': [{'_moId': 'datastore-11',
                                                          'name': '68.25_Local'}],
                                           'guest': {'guestid': None,
                                                     'gueststate': 'notRunning',
                                                     'hostname': None,
                                                     'ipaddress': None},
                                           'name': 'Winserver2008R2_TMP'},
              'vim.VirtualMachine:vm-26': {'config': {'name': 'SDKT_SDKTAP3_7.68.213',
                                                      'template': False},
                                           'datastore': [{'_moId': 'datastore-11',
                                                          'name': '68.25_Local'}],
                                           'guest': {'guestid': 'windows7Server64Guest',
                                                     'gueststate': 'running',
                                                     'hostname': 'HCDCSSDKTAP3',
                                                     'ipaddress': '9.7.68.213'},
                                           'name': 'SDKT_SDKTAP3_7.68.213'},
              'vim.VirtualMachine:vm-32': {'config': {'name': 'RHEL6.5_Temp',
                                                      'template': True},
                                           'datastore': [{'_moId': 'datastore-11',
                                                          'name': '68.25_Local'}],
                                           'guest': {'guestid': None,
                                                     'gueststate': 'notRunning',
                                                     'hostname': None,
                                                     'ipaddress': None},
                                           'name': 'RHEL6.5_Temp'}},
 'SDK_TEST2': {'name': 'SDK_TEST2',
               'vim.VirtualMachine:vm-36': {'config': {'name': 'SDKT_SDKTAP1_7.68.211',
                                                       'template': False},
                                            'datastore': [{'_moId': 'datastore-35',
                                                           'name': '68.28_Local'}],
                                            'guest': {'guestid': 'rhel7_64Guest',
                                                      'gueststate': 'running',
                                                      'hostname': 'HCDCSSDKTAP1',
                                                      'ipaddress': '9.7.68.211'},
                                            'name': 'SDKT_SDKTAP1_7.68.211'},
               'vim.VirtualMachine:vm-37': {'config': {'name': 'SDKT_SDKTAP2_7.68.212',
                                                       'template': False},
                                            'datastore': [{'_moId': 'datastore-35',
                                                           'name': '68.28_Local'}],
                                            'guest': {'guestid': 'rhel6_64Guest',
                                                      'gueststate': 'running',
                                                      'hostname': 'HCDCSSDKTAP2',
                                                      'ipaddress': '9.7.68.212'},
                                            'name': 'SDKT_SDKTAP2_7.68.212'}}}


class genIniData():
    def __init__(self,indict):
        self.indict = indict
    def to_Ini_Linux(self):
        print(type(self.indict))
        print(self.indict)

if __name__ == "__main__":

    start_time = datetime.datetime.now()
    global final_facts
    final_facts = {}
    # genIniData(result).to_Ini_Linux()
    
    
    main()

    with open ("%s/tmp_file/all_vm_facts.txt"%(os.path.dirname(__file__)),"w+") as f:
        f.write(pprint.pformat(final_facts))
    
    
    end_time = datetime.datetime.now()

    print('\n开始时间:%s ---> 结束时间:%s \n时间差为:%s'%(start_time, end_time, (end_time - start_time)))