###
# File: db_pymysql.py
# Created Date: 2020-11-30
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Saturday December 5th 2020 6:04:45 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
from contextlib import contextmanager
import pymysql

db_config={
    "host":"localhost",
    "user":"liuqd",
    "password":"liuquandong",
    "database":"liuqd"
}

@contextmanager
def get_connection(*args, **kwargs):
    connection = pymysql.connect(*args, **kwargs)
    try:
        yield connection
    finally:
        connection.close()

class db_connection_adv:
    def __init__(self,*args, **kwargs):
        self.connection = pymysql.connect(*args, **kwargs)
    def __enter__(self,*args, **kwargs):
        return self.connection
    def __exit__(self, exc_t, exc_v, traceback):
        if exc_t:
            print("出错了:",exc_v)
            self.connection.close()
            return True
        else:
            print("执行完毕,数据库连接会被关闭")
            self.connection.close()


if __name__ == "__main__":
    sql = "show index from student"
    sql_except = """
    INSERT INTO TABLEGOGO(name, age, phone)
        VALUES ('juddy', 35, 17722356765)
    """
    sql_multiple = """
    INSERT INTO student(name, age, phone)
        VALUES (%s, %s, %s)
    """
    data = [("tom", 41, 18766778908 ),("alex",15, 13078690986 )]
    # with get_connection(**db_config) as con:
    #     with con.cursor() as cur:
    #         cur.execute(sql)
    #         print(cur.fetchall())
    with db_connection_adv(**db_config) as con:
        cur = con.cursor()
        # cur.execute(sql_except)
        cur.execute(sql)
    # with get_connection(**db_config) as con:
    #     with con.cursor() as cur:
    #         try:
    #             cur.execute(sql_except)
    #             con.commit()
    #         # except cur.ProgrammingError as err:
    #         except Exception as err:
    #             con.rollback()
    #             print(err)
    # with get_connection(**db_config) as con:
    #     with con.cursor() as cur:
    #         try:
    #             cur.executemany(sql_multiple,data)
    #             con.commit()
    #         # except cur.ProgrammingError as err:
    #         except Exception as err:
    #             con.rollback()
    #             print(err)    
