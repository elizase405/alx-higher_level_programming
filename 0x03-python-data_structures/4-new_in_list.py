#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copied_list = my_list

    if idx < 0 or idx > len(my_list):
        return copied_list

    new_list = [my_list[i] for i in range(len(my_list))]

    new_list[idx] = element
    return new_list
