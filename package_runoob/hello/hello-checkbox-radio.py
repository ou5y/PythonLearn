#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-

# 引入 CGI 处理模块
import cgi, cgitb

# 创建 FieldStorage的实例
form = cgi.FieldStorage()

# 接收字段数据
if form.getvalue('google'):
    google_flag = "是"
else:
    google_flag = "否"

if form.getvalue('runoob'):
    runoob_flag = "是"
else:
    runoob_flag = "否"

if form.getvalue('site'):
    site = form.getvalue('site')
else:
    site = "提交数据为空"

print "Content-type:text/html"
print
print "<html>"
print "<head>"
print "<meta charset=\"utf-8\">"
print "<title>菜鸟教程 CGI 测试实例</title>"
print "</head>"
print "<body>"
print "<h2> 复选框--菜鸟教程是否选择了 : %s</h2>" % runoob_flag
print "<h2> 复选框--Google 是否选择了 : %s</h2>" % google_flag
print "<br>"
print "<h2> 单选框--选择了 : %s</h2>" % site
print "</body>"
print "</html>"
