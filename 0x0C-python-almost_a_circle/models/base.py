#!/usr/bin/python3
"""
This module defines 1 class:
    b = Base()
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns a string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    def from_json_string(json_string):
        """ returns a list representation of the json string """
        if not json_string or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation
        of list_objs to a file
        """

        filename = "{}.json".format(cls.__name__)
        list_dic = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

        str_list_obj = cls.to_json_string(list_dic)

        with open(filename, "w") as f:
            f.write(str_list_obj)
