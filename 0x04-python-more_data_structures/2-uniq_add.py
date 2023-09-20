#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_lst = set(my_list)
    total = 0

    for x in uniq_lst:
        total+=x

    return total
