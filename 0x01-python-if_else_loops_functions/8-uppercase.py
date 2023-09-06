#!/usr/bin/python3
def uppercase(c):
    for i in c:
        asc = ord(i) - 32
        if asc >= 65 and asc <= 90:
            pass
        else:
            asc = asc + 32
        print("{:c}".format(asc), end="")
    print("\n", end="")
