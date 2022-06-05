#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = number % -10
else:
    last = number % 10
print('last digit of {} is '.format(numbers), end="")
is last > 5:
    print('{} and is greater than 5' .format(last))
elif last  == 0:
    print('{} and is 0' .format(last))
elif last < 6 and last != 0:
    print('{} and is less than 6 and 0' .format(last))

