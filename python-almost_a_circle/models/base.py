#!/usr/bin/python3
""" doc file base class
"""
import json


class Base:
    """ class base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ use the json lib to convert python obj to json string """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ this fn write to a file the list of instance of class
            to_dict -> a dict of attribute
            to_json_string -> transform a dict to string
        """
        if cls.__name__ == "Rectangle":
            file_name = "Rectangle.json"
        if cls.__name__ == "Square":
            file_name = "Square.json"

        with open(file_name, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write("[")
                for key, item in enumerate(list_objs):
                    f.write(item.to_json_string(item.to_dictionary()))
                    if key != len(list_objs) - 1:
                        f.write(", ")
                f.write("]")

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return "[]"
        return json.loads(json_string)
