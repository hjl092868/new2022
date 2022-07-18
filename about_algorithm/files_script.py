# -*- coding: utf-8 -*-
import os
import os.path


# 遍历拿到某路径下的所有文件
# 参考https://blog.csdn.net/weixin_41845437/article/details/120497110
# os.walk,参考https://www.runoob.com/python/os-walk.html

rootdir = '/Users/hjl/HJLPrivate/new2022'
for parent, dirnames, filenames in os.walk(rootdir):
    num = 1
    for filename in filenames:
        print(f'{num} parent is {parent}')
        print(f'{num} filename is {filename}')
        num += 1
