#!/usr/bin/python3
from models.base import Base

"""
This module defines 1 class that is
a subclass of the Base class:
    r = Rectangle()
"""


class Rectangle(Base):
    """
    Class Rectangle.

    Args: Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes the data """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """ returns the area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """
        prints in stdout the Rectangle instance
        with the character #
        """

        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    @property
    def width(self):
        """ gets width. """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets width. """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ gets height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height. """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ gets x. """
        return self.__x

    @x.setter
    def x(self, value):
        """ sets x. """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ gets y. """
        return self.__y

    @y.setter
    def y(self, value):
        """ sets y. """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __str__(self):
        """ returns output when str() or print() is used """

        cls = "[Rectangle] "
        idd = "({}) ".format(self.id)
        xy = "{}/{} - ".format(self.x, self.y)
        wh = "{}/{}".format(self.width, self.height)

        return cls + idd + xy + wh

