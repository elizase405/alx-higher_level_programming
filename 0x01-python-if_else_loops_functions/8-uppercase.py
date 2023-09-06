#!/usr/bin/python3
def uppercase(c):
    for i in c:
        asc = ord(i) - 32
        if asc >= 65 and asc <= 90:
            print(f"{chr(asc)}", end="")
        else:
            print(f"{i}", end="")
    print("\n", end="")
