#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for k in sorted(a_dictionary):
        v = a_dictionary[k]
        print("{:s}: {}".format(k, v))
