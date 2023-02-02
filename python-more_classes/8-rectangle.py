#!/usr/bin/python3
""" Doc
"""


class Rectangle:
    """ class for rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_2

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
                print("{}".format(self.print_symbol), end="")
            if longeur + 1 == self.height:
                pass
            else:
                print()
        return ""

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
