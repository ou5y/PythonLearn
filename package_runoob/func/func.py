# encoding=utf-8

import types


def add(x, y, f):
    return f(x), f(y), f(x) + f(y)


def print_func():
    print add(-9, -18, abs)


def f(x):
    return x * x


def print_f():
    print map(f, range(1, 11, 1))


print_func()

print_f()

print map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print range(1, 4)


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()

print f1()

print f2()

list = ["one", "two", "three"]

m, n, o = list

print m, n, o


def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            print "i的值是：%d" % j

            def g():
                return j * j

            return g

        fs.append(f(i))  # 这儿其实append的是函数g，参数是动态的i
    return fs


f1, f2, f3 = count()
print f2()

print map(lambda x: x * x, range(1, 11, 1))

xy = lambda x, y: x * x + y * y
print xy(2, 3)


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)

        return wrapper

    return decorator


@log('自定义描述')
def now():
    print '2013-12-25'


now()


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    @property
    def score(self):
        return self.score

    @score.setter
    def score(self, val):
        if not val and (isinstance(val, int) or type(val) == types.IntType):
            self.score = val
        else:
            val = -1


def setJJWW2(self, text):  # 虽然这是类外部的方法，但是也得要有一个sefl参数才行（实际上也是一个参数）
    print self
    print text


Student.setJJWW = types.MethodType(setJJWW2, None, Student)  # 别人的方法、Obj对象(给类定义的时候不需要)、类
bart = Student('Bart Simpson', 59)
bart.setJJWW('321321')

bart.age = 8
bart.xqgg = 321
print bart.name  # 输出Bart Simpson
print bart.age  # 输出8
print bart.xqgg  # 输出321
