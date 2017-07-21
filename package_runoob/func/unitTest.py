# encoding=utf-8

import unittest
from Dict import Dict


class TestDict(unittest.TestCase):
    def setUp(self):
        print 'setUp...'

    def tearDown(self):
        print 'tearDown...'

    def test_init(self):
        print 'test_init'
        d = Dict(a=1, b='test')
        # print d.a
        # print type(d.a)
        self.assertEquals(d.a1, 1)  # 断言函数返回的结果与1相等
        self.assertEquals(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        print 'test_key'
        d = Dict()
        d['key'] = 'value'
        self.assertEquals(d.key, 'value')

    def test_attr(self):
        print 'test_attr'
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEquals(d['key'], 'value')

    def test_keyerror(self):
        print 'test_keyerror'
        d = Dict()
        with self.assertRaises(KeyError):  # 期待抛出指定类型的Error，比如通过d['empty']访问不存在的key时，断言会抛出KeyError
            value = d['empty']

    def test_attrerror(self):
        print 'test_attrerror'
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


# if __name__ == '__main__':
#     print '开始测'
#     unittest.main()
