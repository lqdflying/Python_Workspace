# -*- coding: utf-8 -*-
'''
Created on 2018年9月12日

@author: anddy.liu
'''
from aliyunsdkcore.client import AcsClient
#from aliyunsdkcore.acs_exception.exceptions import ClientException
#from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
#from aliyunsdkecs.request.v20140526 import StopInstanceRequest
import sys
import json
import pprint
from config import access_id,access_key_secret
clt = AcsClient(access_id,access_key_secret,'ap-southeast-1')
print(clt)

# 创建 request，并设置参数
# request = DescribeInstancesRequest.DescribeInstancesRequest()
# request.set_PageSize(10)
# request.set_accept_format(json)
# # 发起 API 请求并打印返回
# response = clt.do_action_with_exception(request)
# print(response)
def ecs_info(instanceid,fmt='json'):
    request=DescribeInstancesRequest.DescribeInstancesRequest()
    request.set_accept_format(fmt)
    request.set_InstanceIds([instanceid])
    
    try:
        result=clt.do_action(request)
        r_dict=json.loads(result)
    except:
        print("Get Instance Info Failed.")
        sys.exit()
        
    if 'TotalCount' in r_dict and r_dict['TotalCount'] != 0:
        instance=r_dict['Instances']['Instance'][0]
        return instance
    else:
        print("Instance id %s is not exist.") % instanceid
        sys.exit()
pprint.pprint(ecs_info('i-t4n4hcrego2q960favxk'))