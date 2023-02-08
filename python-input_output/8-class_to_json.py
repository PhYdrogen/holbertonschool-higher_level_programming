#!/usr/bin/python3
""" doc
"""


def class_to_json(obj):
    """ convert an entire class to json format
    """
    return vars(obj)
