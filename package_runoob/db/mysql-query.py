#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-

import MySQLdb
import jdbc

# 打开数据库连接
try:
    db = MySQLdb.connect(jdbc.host, jdbc.username, jdbc.password, jdbc.db)

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 使用execute方法执行SQL语句
    cursor.execute("SELECT * FROM EMPLOYEE WHERE INCOME > %d" % 200)

    print "查询到的行数：%d" % cursor.rowcount

    # 使用 fetchone() 方法获取一条数据库。
    one = cursor.fetchone()  # 返回的是一个tuple元组
    print "只是获取一个的：fname=%s\tlname=%s\tage=%d\tsex=%s\tincome=%d" % \
          (one[0], one[1], one[2], one[3], one[4])

    res = cursor.fetchall()  # 返回的是一个tuple元组

    for row in res:
        print "fname=%s\tlname=%s\tage=%d\tsex=%s\tincome=%d" % \
              (row[0], row[1], row[2], row[3], row[4])

    print 'END'
    # 关闭数据库连接
    db.close()

except BaseException, e:
    print e
