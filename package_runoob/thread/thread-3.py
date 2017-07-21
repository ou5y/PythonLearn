#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-

import threading,multiprocessing
import time

exitFlag = 0


print  multiprocessing.cpu_count()


class myThread(threading.Thread):
    '线程安全的'

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print "Starting\t" + self.name
        # 获得锁，成功获得锁定后返回True
        # 可选的timeout参数不填时将一直阻塞直到获得锁定
        # 否则超时后将返回False
        threadLock.acquire()
        self.print_time(self.name, self.counter, 5)
        # 释放锁
        threadLock.release()
        print "END\t" + self.name

    def print_time(self, threadName, delay, counter):
        while counter:
            print "******\tthreadName：%s\tcounter：%d*******\n" % (threadName, counter)
            if exitFlag:
                threading.Thread.exit()
            time.sleep(delay)
            print "%s: %s" % (threadName, time.ctime(time.time()))
            counter -= 1


threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
# 相当于的js中的alert() 得等它运行完成了后才能运行后面的代码
for t in threads:
    t.join()

print '\nSUCCESS\n'


# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    print 'Hello, %s (in %s)' % (local_school.student, threading.current_thread().name)

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()