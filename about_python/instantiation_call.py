# -*- coding: utf-8 -*-
import functools


class A:
    '''
    new\init\call方法的区别
    '''

    def __new__(cls, *args, **kwargs):
        print('aaa')
        return super().__new__(cls)

    def __call__(self, *args, **kwargs):
        print(222)
        if args[0] == 1:
            print(111)
        else:
            print(333)

    @classmethod
    def use_call(cls, *args):
        def inner(a, b):
            inner_t = cls(*args)
            print(456)
            return inner_t(a, b)
        inner.consumer_class = cls
        inner.consumer_args = args
        functools.update_wrapper(inner, cls, updated=())
        print(345)
        return inner

    def add(self, a, b):
        print(444)
        return a + b

    def test_assert(self, a):
        # assert type(a) is int, 'test_assert参数要为数字'
        # assert type(a) is int
        header = getattr(self, a, None)
        if header:
            print(header, type(header))
        else:
            raise ValueError('该对象没有这个方法')





ins_a = A()
ins_a.add(1,2)
A.use_call(1,333)
# ins_a(1,333)
# ins_a.test_assert('test_assert')