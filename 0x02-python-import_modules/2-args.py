#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    _argv = sys.argv
    argv_len = len(_argv) - 1

    if argv_len == 0:
        print("{:d} arguments.".format(argv_len))
    elif argv_len == 1:
        print("{:d} argument:".format(argv_len))
        print("{0:d}: {1:s}".format(1, _argv[1]))
    else:
        print("{:d} arguments:".format(argv_len))
        for i in range(1, argv_len + 1):
            print("{0:d}: {1:s}".format(i, _argv[i]))
