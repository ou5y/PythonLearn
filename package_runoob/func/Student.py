# encoding=utf-8
import types
import logging

logging.basicConfig(level=logging.INFO)

dict = dict(a=1, b=3, c=dict(d=4))
print dict
list = list((1, 2, 3, 45, 6))
print list

logging.info("nimeide")
print 'after going'


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


def main():
    foo('2')


try:
    main()
except BaseException, e:
    print 'guale'
    print e


class Student(object):
    @property
    def score(self):
        print 'get'
        return self._score

    @score.setter
    def score(self, val):
        print 'set'
        if val and (isinstance(val, int) or type(val) == types.IntType):
            self._score = val
        else:
            self._score = -1

    def __str__(self):
        return 'SS'

    __repr__ = __str__


s = Student()
s
s.score = 66
print s.score
