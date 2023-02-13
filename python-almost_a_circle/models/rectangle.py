#!/usr/bin/python3
""" doc file rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """ rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """ return the area of instance rect """
        return self.__width * self.__height

    def display(self):
        """ print the rect to stdout """
        for Y in range(self.y):
            print()

        for ligne in range(self.height):
            print(" " * self.x if self.x > 0 else "", end="")
            for case in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)

    def update(self, *args):
        """ this we can update rectangle on the go """
        count = 0
        for arg in args:
            if count == 0:
                self.id = arg
            if count == 1:
                self.width = arg
            if count == 2:
                self.height = arg
            if count == 3:
                self.x = arg
            if count == 4:
                self.y = arg
            count += 1
