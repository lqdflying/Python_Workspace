#!_*_coding:utf-8_*_
#__author__:"Alex Li"
import os
from core import db_handler # @UnresolvedImport @UnusedImport
from conf import settings # @UnresolvedImport @UnusedImport
from core import logger  # @UnresolvedImport @UnusedImport
import json
import time



def login_required(func):
    "验证用户是否登录"

    def wrapper(*args,**kwargs):
        #print('--wrapper--->',args,kwargs)
        if args[0].get('is_authenticated'):
            return func(*args,**kwargs)
        else:
            exit("User is not authenticated.")
    return wrapper


def acc_auth(account,password):
    '''
    account auth func
    :param account: credit account number
    :param password: credit card password
    :return: if passed the authentication , retun the account object, otherwise ,return None
    '''
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = "%s/%s.json" %(db_path,account)
    print(account_file)
    if os.path.isfile(account_file):
        with open(account_file,'r') as f:
            account_data = json.load(f)
            if account_data['password'] == password:
                exp_time_stamp = time.mktime(time.strptime(account_data['expire_date'], "%Y-%m-%d"))
                if time.time() >exp_time_stamp:
                    print("Account [%s] has expired,please contact the back to get a new card!" % account)
                else: #passed the authentication
                    return  account_data
            else:
                print("Account ID or password is incorrect!")
    else:
        print("Account [%s] does not exist!" % account)


def acc_auth2(account,password):
    '''
    优化版认证接口
    :param account: credit account number
    :param password: credit card password
    :return: if passed the authentication , retun the account object, otherwise ,return None

    '''
    db_api = db_handler.db_handler()
    data = db_api("select * from accounts where account=%s" % account)


    if data['password'] == password: #这里是为了程序的解耦，防止将来使用其他的方法来做登录接口的验证
        exp_time_stamp = time.mktime(time.strptime(data['expire_date'], "%Y-%m-%d"))
        if time.time() > exp_time_stamp:
            print("Account [%s] has expired,please contact the back to get a new card!" % account)
        else:  # passed the authentication
            return data
    else:
        print("Account ID or password is incorrect!")

def acc_login(user_data,log_obj):
    '''
    account login func
    :user_data: user info data , only saves in memory
    :return:
    '''
    retry_count = 0
    while user_data['is_authenticated'] is not True and retry_count < 3 :
        account = input("account:").strip()
        password = input("password:").strip()
        auth = acc_auth2(account, password)
        if auth: #not None means passed the authentication
            user_data['is_authenticated'] = True
            user_data['account_id'] = account
            #print("welcome")
            return auth
        retry_count +=1
    else:
        log_obj.error("account [%s] too many login attempts" % account)
        exit()
