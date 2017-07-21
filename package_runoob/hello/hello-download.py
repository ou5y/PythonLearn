#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-

# HTTP 头部
print "Content-Disposition: attachment; filename=\"foo.txt\"";
print
# 打开文件
fo = open("D:\foo.txt", "rb")

str = fo.read();
print str

# 关闭文件
fo.close()
