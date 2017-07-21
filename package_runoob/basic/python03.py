# coding=utf-8

import random
import sys
import time

index = 0
arr = []
while index < 10:
    index += 1
    if index % 2 != 0:
        continue
    arr.append(index)
else:
    print '老子跳出循环了'

for temp in arr:
    print '数字：\t', temp, '\t',
print
for temp in range(0, len(arr), 1):
    print '数字：\t', arr[temp], '\t',

print '\nGoodbye Loop'

sequence = [12, 34, 34, 23, 45, 76, 89]
print enumerate(sequence)
for i, j in enumerate(sequence):
    if i == 0:
        continue
    elif i > 3:
        break
    print i, j
