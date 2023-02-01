#!/usr/bin/python3
""" Doc
"""


def text_indentation(text):
    """ Doc
    """
    if type(text) is not str:
        raise TypeError('text must be a string')

    these = ['.', '?', ';']
    for char in text:
        if char in these:
            print(char)
            print()
        else:
            print(char, end="")
