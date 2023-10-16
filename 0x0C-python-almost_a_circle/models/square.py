#!/usr/bin/python3
"""
This module contains 1 class
that inherits from the rectangle class:
    s = Square()
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This is the Square class.

    Args: Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes instance """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ get size """
        return self.height

    @size.setter
    def size(self, value):
        """ set size """
        self.width = value
        self.height = value

    def __str__(self):
        """ returns output when str() or print() is used """

        cls = "[Square] "
        idd = "({}) ".format(self.id)
        xy = "{}/{} - ".format(self.x, self.y)
        wh = "{}/{}".format(self.width, self.height)

        return cls + idd + xy + wh
