#!/usr/bin/python3
def add_integer(a, b=98):
    if type(a) is float or type(a) is int:
        if type(b) is float or type(b) is int:
            return int(a) + int(b)
        else:
            raise TypeError('b must be an integer')
    else:
        raise TypeError('a must be an integer')


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
