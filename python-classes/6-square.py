#!/usr/bin/python3
""" This is my doc square file
"""


class Square:
    """ This is my square class
    """

    def __init__(self, size=0, position=(0, 0)):
        """ this is my init
        """
        self.size = size
        self.position = position

    def area(self):
        """ Return the current square of the area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """ Size Getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Size Setter
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """ Pos Getter
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Pos Setter
        """
        if type(value) is not tuple or len(value) < 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        """ Prints in stdout the square with the character #
        """
        space_pos = " " * self.position[0]
        if self.size == 0:
            print("")
            return
        for saut in range(self.position[1]):
            print()
        for i in range(self.size):
            print("{}".format(space_pos), end="")
            for i in range(self.size):
                print("#", end="")
            print("")
