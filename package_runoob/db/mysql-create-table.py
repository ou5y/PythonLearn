#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-

import MySQLdb
import jdbc

# 打开数据库连接
try:
    db = MySQLdb.connect(jdbc.host, jdbc.username, jdbc.password, jdbc.db)
except BaseException, e:
    print e

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 创建数据表SQL语句
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(2),
         INCOME FLOAT )"""

cursor.execute(sql)

print 'SUCCESS'

# 关闭数据库连接
db.close()
