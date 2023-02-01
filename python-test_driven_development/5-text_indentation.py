#!/usr/bin/python3
""" Doc
"""


def text_indentation(text):
    """ Doc
    """
    if type(text) is not str:
        raise TypeError('text must be a string')

    these = ['.', '?', ':']
    last_char = ''
    for char in text:
        if char in these:
            print(char)
            print()
            last_char = '\n'
        else:
            if last_char == '\n' and char == ' ':
                continue
            print(char, end="")
            last_char = char
