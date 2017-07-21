#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-

import thread
import time


class MyFirstPythonThread:
    # 为线程定义一个函数
    def print_time(self, threadName, delay):
        try:
            count = 0
            while count < 5:
                time.sleep(delay)
                # if count == 4:
                #     thread.exit()
                count += 1
                print "%s: %s" % (threadName, time.ctime(time.time()))
        except BaseException, e:
            print '这个地方异常了'

    def seeXiaoGuo(self):
        print 'come in'
        # thread.start_new_thread(self.print_time("Thread-1", 1))
        thread.start_new_thread(self.print_time("Thread-2", 2))
        print 'come out'

# 创建两个线程
try:
    print_time_obj = MyFirstPythonThread()
    print_time_obj.seeXiaoGuo()
except BaseException, e:
    print '恨自个地方也异常了'
    print e

while 1:
    pass
