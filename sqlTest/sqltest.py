#!/usr/bin/python

#coding=utf-8

import pymysql

import pymysql.cursors

connection=pymysql.connect(host='127.0.0.1',user='hallokael',password='123456a',db='world',port=3306,charset='utf8')
with connection.cursor() as cursor:
    pass
    # sql=u'select * from city'
    #
    # cout=cursor.execute(sql)
    #
    # print("数量:"+str(cout))
    #
    # for row in cursor.fetchall():
    #     print("编号："+str(row[0])+'    名字：'+row[1]+"    性别："+row[2])
    # connection.commit()
    # connection.close()

