#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_num = list(set(my_list))
    result = 0
    for i in range(len(unique_num)):
        result += unique_num[i]
    return result
