#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-

import thread, threading
import time


# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 2:
        time.sleep(delay)
        count += 1
        print "%s: %s" % (threadName, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


# 创建两个线程
try:
    thread.start_new_thread(print_time, ("Thread-1", 1,))
    thread.start_new_thread(print_time, ("Thread-2", 1,))
except:
    print "Error: unable to start thread"

print "*************************"


def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 'thread %s ended.' % threading.current_thread().name


print 'thread %s is running...' % threading.current_thread().name
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print 'thread %s ended.' % threading.current_thread().name
