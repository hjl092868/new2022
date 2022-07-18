# -*- coding: utf-8 -*-
import time


# kmp算法，求出next数组
def next_list(str1: str):
    result_list = []
    for x in range(len(str1)):
        if x == 0:
            result_list.append(0)
        elif x == 1:
            result_list.append(1)
        else:
            child_str = str1[:x]
            len_child_str = len(child_str)
            len_result = 0
            i = 1
            while i < len_child_str:
                if child_str[:i] == child_str[-i:]:
                    len_result = i
                i += 1
            result_list.append(len_result + 1)
    return result_list


# str1 = 'ababaaaba'
# result_list = next_list(str1)
# print(result_list)


# 判断是否相等
def kmp(str1: str, str2: str):
    next_list_str2 = next_list(str2)

    len_str1 = len(str1)
    len_str2 = len(str2)
    x = 0
    # for x in range(len_str1):
    while x <= len_str1 - len_str2 + 1:
        i = 1
        while i <= len_str2:
            if str1[x:x+i] != str2[:i]:
                break
            if i == len_str2 and str1[x:x+i] == str2[:i]:
                return x
            i += 1
        next_i = next_list_str2[i-1]
        if next_i == 0:
            next_i = 1
        print(x, next_i, i)
        time.sleep(2)
        x += next_i
    return 0



str1 = 'abcababxcabcabx'
str2 = 'abx'
result = kmp(str1, str2)
print(result)
