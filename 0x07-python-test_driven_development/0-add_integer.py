#!/usr/bin/python3

"""This is the add_integer module.
This module defines 1 function:
    add_integer(1, 2)
    3
"""


def add_integer(a, b=98):
    """Adds 2 integer or float values together.
    The floats are casted to ints before addition
    """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
