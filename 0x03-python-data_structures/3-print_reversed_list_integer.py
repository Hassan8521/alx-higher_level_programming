#!/usr/bin/python3
def print_reverse_list_integer(my_list=[]):
    if not my_list:
        return
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
