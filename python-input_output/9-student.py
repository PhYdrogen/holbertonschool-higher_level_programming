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

    def to_json(self):
        return vars(self)
