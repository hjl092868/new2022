# -*- coding: utf-8 -*-
# 冒泡排序
# O(n2)


def maopaosort(lst:list):
    if len(lst) <= 1:
        return lst
    for n in range(len(lst)-1):
        if lst[n] > lst[n+1]:
            lst[n], lst[n+1] = lst[n+1], lst[n]
    return maopaosort(lst[:-1]) + [lst[-1]]


list1 = [2,5,1,66,73,4,2,5,567,3,82,52,0]
list2 = maopaosort(list1)
print(list2)
