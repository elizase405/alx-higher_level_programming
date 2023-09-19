#!/usr/bin/python3
def search_replace(my_list, search, replace):
    lst = []

    for i in my_list:
        if i == search:
            i = replace
        lst.append(i)

    return lst
