#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" File for rectangle class
"""


class Rectangle(BaseGeometry):
    """ Rectangle class of base geometry
    """
    def __init__(self, width, height):
        """ init rectangle
        """
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
