#!/usr/bin/python3
""" This is my doc square file
"""


class Square:
    """ This is my square class
    """

    def __init__(self, size=0):
        """ this is my init
        """
        self.__size = size

    def area(self):
        """ Return the current square of the area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """ Getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def my_print(self):
        """ Prints in stdout the square with the character #
        """
        if self.size() == 0:
            print("")
            return

        for i in range(self.size()):
            for i in range(self.size()):
                print("#", end="")
            print("")
