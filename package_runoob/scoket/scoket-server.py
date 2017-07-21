#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-

import socket  # 导入 socket 模块
import time, threading


def tcplink(sock, addr):
    # addr : <type 'tuple'>: ('192.168.114.1', 9309)
    print '%s访问了我' % addr[0]
    sock.send('%s欢迎访问菜鸟教程！%s' % (addr[0], time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
    sock.close()  # 关闭连接


# 创建 socket 对象 AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议
s = s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()  # 获取本地主机名
port = 12345  # 设置端口
print "我host：%s\tport：%d准备好了，client们来访问我吧" % (host, port)
s.bind((host, port))  # 绑定需要被监听的IP和端口

s.listen(5)  # 等待客户端连接

while True:
    sock, addr = s.accept()  # 建立客户端连接。并会等待且返回一个客户端的连接
    # 每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接：
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
