#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def width(self):
        return self.__width

    def width(self, value):
        if type(value) != int:
            print("width must be an integer")
            raise TypeError
        if value > 0:
            print("width must be >= 0")
            raise ValueError
        self.__width = value

    def height(self):
        return self.__height

    def height(self, value):
        if type(value) != int:
            print("height must be an integer")
            raise TypeError
        if value > 0:
            print("height must be >= 0")
            raise ValueError
        self.__height = value
