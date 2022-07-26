# -*- coding:utf-8 -*-
from functools import update_wrapper


def fun(func):
    def inner(*args, **kwargs):
        print(inner.__name__)
        return func(*args, **kwargs)
    # 如果注释掉下面这一样，这下面的print出来的对象都是显示inner这个方法名
    # update_wrapper(inner, func, updated=())
    return inner


@fun
def add_self(a, b):
    return a + b


print(add_self)
print(add_self(2, 3))


def sub_self(a, b):
    return a - b


print(fun(sub_self))