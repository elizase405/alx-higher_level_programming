#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
A module with 1 function
"""

class Rectangle(BaseGeometry):
    """ Class that defines a rectangle from BaseGeometry Class """

    def __init__(self, width, height):
        """ Initializes instance """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
