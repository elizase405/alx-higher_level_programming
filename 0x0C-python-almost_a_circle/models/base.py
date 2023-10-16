#!/usr/bin/python3

"""
This module defines 1 class:
    b = Base()
"""


class Base:
    """
    Base class.
    Class that manages id attributes of child classes
    and avoid duplicating the same code(by extension, same bugs).

    Args: None
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes the data """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
