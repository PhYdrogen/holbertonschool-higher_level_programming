#!/usr/bin/python3
""" Doc
"""


def print_square(size):
    """ print a square
    """

    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for ligne in range(size):
        for dieze in range(size):
            print('#', end="")
        print()
