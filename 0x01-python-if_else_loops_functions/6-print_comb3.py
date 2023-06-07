#!/usr/bin/python3
for num in range(0, 10):
    for su in range(num + 1, 10):
        if num == 8 and su == 9:
            print("{}{}".format(num, su))
        else:
            print("{}{}".format(num, su), end=", ")
