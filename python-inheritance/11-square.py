#!/usr/bin/python3
""" File for rectangle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class of base Rectangle
    """
    def __init__(self, size):
        """ init square
        """
        try:
            super().integer_validator("size", size)
            self.__size = size

        except Exception as e:
            print(e)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[Square] {0}/{0}".format(self.__size)
