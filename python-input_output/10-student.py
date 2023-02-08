#!/usr/bin/python3
""" doc
"""


class Student:
    """ class for student
    """
    def __init__(self, fn, ln, age):
        """ init method
        """
        self.first_name = fn
        self.last_name = ln
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return vars(self)
        else:
            dict_attrs = vars(self)
            new_dict = dict()
            for arg in attrs:
                if arg in dict_attrs:
                    new_dict[arg] = dict_attrs.get(arg)
            return new_dict
