# encoding=utf-8
from multiprocessing import Process, Pool, Queue
import os, time, random


# 为父线程创建子线程
# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动
def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())


if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    p = Process(target=run_proc, args=('子线程名称',))
    print 'Process will start.'
    p.start()
    p.join()
    print 'Process end.'


# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
# 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))


if __name__ == '__main__':
    print '测试进程池——Parent process %s.' % os.getpid()
    p = Pool()  # 由于Pool的默认大小是CPU的核数   p = Pool(number)
    for i in range(1, 11, 1):
        p.apply_async(long_time_task, args=("线程-%d" % i,))
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'


# 进程间通信
# 写数据进程执行的代码:
def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码:
def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程，以便于进程间的通讯：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
