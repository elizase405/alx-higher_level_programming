#!/usr/bin/python3
"""This say_my_name module contains 1 function: say_my_name()
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a string with first_name and last_name

    Args:
        first_name (str) the first name to be printed
        last_name (str) the last name to be printed

    Raises:
        TypeError: raised if first_name and last_name are not strings.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
