#!/usr/bin/python3
def uniq_add(my_list=[]):
    x_list = set(my_list)
    result = 0
    for a in x_list:
        result += a
    return result
