# encoding=UTF-8
import time;
import calendar;


arr = [x*5 for x in range(2,10,2)]
print arr

def getCurrentTime(localTime):
    str = time.strftime("%Y-%m-%d %H:%M:%S", localTime)
    return str

currDate = getCurrentTime(time.localtime(time.time()))

print currDate


def printme(name, age='89岁', *sex):
    print name, age


printme(age='55岁', name='王麻子')

printme('张二娃')

printme('田伯光', '44', '女的', '312')

sum = lambda arg1, arg2: arg1 + arg2;

print "相加后的值为 : ", sum(10, 20)

