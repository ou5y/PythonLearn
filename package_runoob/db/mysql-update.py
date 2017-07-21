#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-

import MySQLdb
import jdbc

# 打开数据库连接
try:
    db = MySQLdb.connect(jdbc.host, jdbc.username, jdbc.password, jdbc.db)

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 更新年龄大于50的员工的工资+1000
    cursor.execute("SELECT * FROM EMPLOYEE WHERE AGE >= %d" % 50)
    print "年龄大于50的员工有：%d" % cursor.rowcount
    res = cursor.fetchall()
    for row in res:
        print "fname=%s\tlname=%s\tage=%d\tsex=%s\tincome=%d" % \
              (row[0], row[1], row[2], row[3], row[4])

    cursor.execute("UPDATE EMPLOYEE SET INCOME = INCOME + 1000 WHERE AGE >= %d" % 50)
    print
    print "被更新工资人数：%d" % cursor.rowcount

    cursor.execute("SELECT * FROM EMPLOYEE WHERE AGE >= %d" % 50)
    print
    print "更新后的员工信息："
    res = cursor.fetchall()
    for row in res:
        print "fname=%s\tlname=%s\tage=%d\tsex=%s\tincome=%d" % \
              (row[0], row[1], row[2], row[3], row[4])


    db.commit()

    print
    print 'END'
    # 关闭数据库连接
    db.close()

except BaseException, e:
    db.rollback()
    print e
