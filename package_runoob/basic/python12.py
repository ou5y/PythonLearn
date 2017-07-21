# encoding=utf-8

import python10

print python10.Employee._empCount2

class Vector:
    '运算符重写'

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

    def prt(self):
        print "a :%d\tb:%d" % (self.a, self.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
v3 = v1 + v2;
v3.prt();
