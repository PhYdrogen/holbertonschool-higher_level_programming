#!/usr/bin/python3
""" File for empty class
"""


class BaseGeometry:
    """ Doc
    """

    def __init__(self):
        pass

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) is bool:
            raise TypeError('[TypeError] {} must be an integer'.format(name))
        if not isinstance(value, int):
            raise TypeError('[TypeError] {} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('[ValueError] {} must be greater than 0'
                             .format(name))
