#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
d = abs(number) % 10
if number < 0:
    d = -d
    print("Last digit of {} is {} and is less than 6".format(number, d))
elif d > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, d))
elif d == 0:
    print("Last digit of 0 is 0 and is 0")
else:
    print("is less than 6 and not 0".format(number, d))
