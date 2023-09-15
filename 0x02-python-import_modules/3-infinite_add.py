#!/usr/bin/python3
import sys

_argv = sys.argv
sum = 0
argv_len = len(_argv)

if argv_len == 1:
    print("{:d}".format(sum))
else:
    for i in range(1, argv_len):
        sum += int(_argv[i])
    print("{:d}".format(sum))
