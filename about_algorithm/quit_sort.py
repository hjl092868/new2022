# -*- coding: utf-8 -*-
# 快速排序
# O(nlogn)


def quitsort(lst:list):
    if len(lst) <= 1:
        return lst
    small = [x for x in lst[1:] if x < lst[0]]
    big = [x for x in lst[1:] if x >= lst[0]]
    return quitsort(small) + [lst[0]] + quitsort(big)


list1 = [2,3,5,61,4,6,6,84,7]
list2 = quitsort(list1)
print(list2)
