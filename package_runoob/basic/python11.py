# encoding=utf-8
import re

import python10

a = 40  # 创建对象  <40>
b = a  # 增加引用， <40> 的计数
c = [b]  # 增加引用.  <40> 的计数

del a  # 减少引用 <40> 的计数
b = 100  # 减少引用 <40> 的计数
c[0] = -1  # 减少引用 <40> 的计数


class Point(python10.Employee, Exception):
    def __init__(self, x=0, y=0):
        super(Point, self).__init__('王麻子', '500万', '99岁')
        self.x = x
        self.y = y
        print '子类构造'

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "销毁"

    def displayEmpInfo(self):
        super(Point, self).displayEmpInfo()
        print '子类打印员工信息'
        print "Name : ", self.name, ", Salary: ", self.salary, "Age %s" % self.age

    def otherMethod(self):
        pt1 = Point()

        print
        pt1.displayEmpInfo()

        pt2 = Point()
        pt2.__setattr__("name", "李四")
        setattr(pt2, "age", "-994岁")
        pt2.displayEmpInfo()

        print
        print pt2.displayEmpCount2()
        print pt1._Employee__empCount
        print python10.Employee._empCount2

    def regx(self):
        print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
        print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配


# print issubclass(Point, python10.Employee)
# print isinstance(pt1, Point)

pt1 = Point()
pt1.regx()
# pt2 = pt1
# pt3 = Point()
# print id(pt1)
# print id(pt2)
# print id(pt3)  # 打印对象的id
# del pt1
# del pt2
# del pt3
