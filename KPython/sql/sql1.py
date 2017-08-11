#!/usr/bin/python
#coding=utf-8

import MySQLdb
import getpass
#输入密码
password = getpass.getpass("Please input your password:")

#打开数据库
try:
    db = MySQLdb.connect('localhost','root',password,'kang')
except ProgrammingError:
    exit(1)


#获取数据库游标
cursor = db.cursor()

try:
    cursor.execute("select * from kang")
    # data = cursor.fetchone()
    # print data
    # data = cursor.fetchone()
    # print data
    # data = cursor.fetchone()
    # print data
    # data = cursor.fetchone()
    # print data
    #
    data = cursor.fetchall()
    # print data
    # print dir(cursor)

    for i in cursor.description:
        print i[0],
    print ""

    for row in data:
        for i in row:
            print i,
        print ""

except:
    print "Error:unable to fecth date"

db.close
