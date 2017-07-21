#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-

import MySQLdb
import jdbc

# 打开数据库连接
try:
    db = MySQLdb.connect(jdbc.host, jdbc.username, jdbc.password, jdbc.db)

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 删除年龄小于50的员工的工资+1000
    cursor.execute("DELETE FROM EMPLOYEE WHERE AGE < %d" % 50)
    print "被删除年龄小于50的员工有：%d" % cursor.rowcount

    db.commit()

    print
    print 'END'
    # 关闭数据库连接
    db.close()

except BaseException, e:
    db.rollback()
    print e
