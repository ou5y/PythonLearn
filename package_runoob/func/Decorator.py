#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-

import cStringIO as stringIO
import imageop

im = imageop.open('1.png')
print im.format, im.size, im.mode
im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')


def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper


# @log
def now():
    print '2013-12-25'


#
#
# now()

log(now)()
