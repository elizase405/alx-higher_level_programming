#!/usr/bin/python3
"""Defining a rectanlge class"""


class Rectangle:
    """Represent a Rectangle claiss"""

    def __init__(self, width=0, height=0):
        """ initializes instance """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns object width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets object width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value > 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets object height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets object height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value > 0:
            rasie ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of object"""
        return self.height * self.width

    def perimeter(self):
        """Returns perimeter of object"""
        return (2 * self.height) + (2 * self.width)

    def __str__(self):
        """ output when str or print method is used"""
        for i in self.height:
            for j in self.width:
                print("#", end="")
            print()
