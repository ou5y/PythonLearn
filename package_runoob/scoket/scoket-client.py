#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-

import socket  # 导入 socket 模块

# 创建 socket 对象 AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议
s = s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()  # 获取本地主机名
port = 12345  # 设置端口好

s.connect((host, port))
res = s.recv(1024342)
print res
s.close()

print '客户端访问完毕'
