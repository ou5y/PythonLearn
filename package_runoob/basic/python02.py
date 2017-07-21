# coding=utf-8
import random
import sys
import time

# a = 5555
# b = 5555
# print a is b
# print a == b
#
# a = 0
# b = 20
#
# c = a and b
# d = a or b
# print c  # 20
# print d  # 10
#
# if a or b:
#     print 'success'
# else:
#     print 'failure'
#
# if 0 and 1:
#     print '对的'
# else:
#     print '''\t错的
#     guad分edfd分sfds分'''

index = 0
arr = [55]
while index < 10:
    index += 1
    if index % 2 != 0:
        continue
    arr.append(index)
    print index
else:
    print '老子跳出循环了'
print 'Goodbye While'

s = int(random.uniform(1, 10))
m = int(input('输入整数:'))
while m != s:
    if m > s:
        print('大了')
        m = int(input('输入整数:'))
    if m < s:
        print('小了')
        m = int(input('输入整数:'))
    if m == s:
        print('OK')
        break;

result = []
while True:
    result.append(int(random.uniform(1, 7)))
    result.append(int(random.uniform(1, 7)))
    result.append(int(random.uniform(1, 7)))
    print result
    count = 0
    index = 2
    pointStr = ""
    while index >= 0:
        currPoint = result[index]
        count += currPoint
        index -= 1
        pointStr += " "
        pointStr += str(currPoint)
    if count <= 11:
        sys.stdout.write(pointStr + " -> " + "小" + "\n")
        time.sleep(1)  # 睡眠一秒
    else:
        sys.stdout.write(pointStr + " -> " + "大" + "\n")
        time.sleep(1)  # 睡眠一秒
    result = []
