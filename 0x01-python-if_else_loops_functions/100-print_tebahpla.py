#!/usr/bin/python3
for i in range(ord('z'), ord('a') -1, -1):
    char = chr(1)
    if 1 % 2 != 0:
        char = chr(i - 32)
        print("{}".format(char), end=' ')
