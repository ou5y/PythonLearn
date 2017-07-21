# encoding=UTF-8
import time;
import calendar;

print '中文的'

localtime = time.localtime(time.time())
print "本地时间为 :", localtime

localtime = time.asctime(time.localtime(time.time()))
print "本地时间为 :", localtime

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
print time.mktime(time.strptime(localtime,"%a %b %d %H:%M:%S %Y"))

cal = calendar.month(2016, 1)
print cal;