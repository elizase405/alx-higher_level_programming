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
        wh = "{}".format(self.size)

        return cls + idd + xy + wh

    def update(self, *args, **kwargs):
        """
        Using no-keyword argument styling
        to assigns an argument to each attribute.

        Args:
            *args - a list on unknown arguments
            **kwargs - a dictionary of unknown arguments
        """
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])

    def to_dictionary(self):
        """ returns dictionary representation of a Square"""
        dictt = {
                'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y,
                }
        return dictt
