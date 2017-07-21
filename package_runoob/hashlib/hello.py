#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-

import hashlib

# MD5
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?')
print md5.hexdigest()  # d26a53750bc40b38b65a520292f69306

# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
md5 = hashlib.md5()
md5.update('how to use md5 in ')
md5.update('python hashlib?')
# 和md5.update('how to use md5 in python hashlib?')相等
print md5.hexdigest()  # d26a53750bc40b38b65a520292f69306

# SHA1
# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
# 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法越慢，而且摘要长度更长。
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in ')
sha1.update('python hashlib?')
print sha1.hexdigest()  # 2c76b57293ce30acef38d98f6046927161b46a44
