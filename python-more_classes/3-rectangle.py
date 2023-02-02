#!/usr/bin/python3
""" Doc
"""


class Rectangle:
    """ class for rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        return 2*(self.height + self.width)

    def __str__(self):
        if self.height == 0 or self.width == 0:
            return ""

        for longeur in range(self.height):
            for case in range(self.width):
                print("#", end="")
            if longeur + 1 == self.height:
                pass
            else:
                print()
        return ""
