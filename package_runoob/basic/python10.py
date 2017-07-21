# encoding=utf-8
import __builtin__


class Employee(Exception):
    '员工salary对照'

    __empCount = 0
    _empCount2 = 456

    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age
        Employee.__empCount += 1
        # print Employee.__name__
        # print self.__module__
        print self.__class__
        print self.__class__.__name__
        # print Employee.__bases__
        # print Employee.Employee__dict__
        print "员工类构造方法运行完毕"

    def __displayEmpCount(self):
        print "Total Employee %d" % self.__empCount

    def displayEmpCount2(self):
        print "Total Employee %d" % self.__empCount

    def displayEmpInfo(self):
        print '父类打印员工信息'
        print "Name : ", self.name, ", Salary: ", self.salary, "Age %s" % self.age



        # print '\n'
        # "创建 Employee 类的第一个对象"
        # emp1 = Employee("Zara", 2000, 20)
        # emp1.displayEmpInfo()
        #
        # print hasattr(emp1, 'age')  # 如果存在 'age' 属性返回 True。
        # print getattr(emp1, 'age')  # 返回 'age' 属性的值
        # print setattr(emp1, 'age', 8)  # 添加属性 'age' 值为 8
        # print emp1.age
        # print delattr(emp1, 'age')
        #
        # print '\n'
        # "创建 Employee 类的第二个对象"
        # emp2 = Employee("Manni", 5000, 4546)
        # emp2.displayEmpInfo()
        #
        # try:
        #     print emp2.age
        #     print hasattr(emp1, 'age')  # 如果存在 'age' 属性返回 True。
        #     print emp1.age
        # except Exception, e:
        #     print '有异常'
        #     print e
        #
        # print __builtin__.getattr(emp2, 'salary')
        #
        # print "Total Employee %d" % Employee.empCount

print dir(Employee)