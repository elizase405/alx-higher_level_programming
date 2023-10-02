#!/usr/bin/python3
"""Defining a rectanlge class"""


class Rectangle:
    """Represent a Rectangle claiss"""


    def __init__(self, width=0, height=0):
        """mwthod to initializes the object created from this class"""


        self.__width = width
        self.__height = height

    def width(self):
        """Returns object width"""
        

        return self.__width

    def width(self, value):
        """Sets object width"""
        

        if type(value) != int:
            print("width must be an integer")
            raise TypeError
        if value > 0:
            print("width must be >= 0")
            raise ValueError
        self.__width = value

    def height(self):
        """Gets object height"""
        

        return self.__height

    def height(self, value):
        """Sets object height"""
        

        if type(value) != int:
            print("height must be an integer")
            raise TypeError
        if value > 0:
            print("height must be >= 0")
            raise ValueError
        self.__height = value

    def area(self):
        """Returns area of object"""


        return height * width

    def perimeter(self):
        """Returns perimeter of object"""


        return (2 * height) + (2 * width)
