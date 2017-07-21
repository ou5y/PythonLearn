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
sql1 = """INSERT INTO EMPLOYEE
(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) 
VALUES 
('Z', 'S', '59', 'W', '5962256')
"""

sql2 = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       ('Mac', 'Mohan', 20, 'M', 2000)

print sql1
print
print sql2

try:
    # 执行sql语句
    cursor.execute(sql1)
    cursor.execute(sql2)
    # 提交到数据库执行
    db.commit()
except BaseException, e:
    # Rollback in case there is any error
    print e
    db.rollback()

print "SUCCESS"

# 关闭数据库连接
db.close()

