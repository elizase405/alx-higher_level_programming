#!/usr/bin/python3
class BaseGeometry:
    """ Class that defines the attributes of Geometric Shapes """

    def area(self):
        """ Method that defines the area of a geomtric shape """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method that recieves the value property

        Árgs:
            name: name of the object
            value: value of the property
