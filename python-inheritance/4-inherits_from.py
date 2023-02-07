#!/usr/bin/python3
""" Doc
"""


def inherits_from(obj, a_class):
    """Doc
    """
    if a_class is type(obj):
        return False
    else:
        return issubclass(type(obj), a_class)
