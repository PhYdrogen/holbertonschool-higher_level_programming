#!/usr/bin/python3
""" File for rectangle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class of base geometry
    """
    def __init__(self, width, height):
        """ init rectangle
        """
        try:
            super().integer_validator("width", width)
            self.__width = width

        except Exception as e:
            print(e)
        try:
            super().integer_validator("height", height)
            self.__height = height

        except Exception as e:
            print(e)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
