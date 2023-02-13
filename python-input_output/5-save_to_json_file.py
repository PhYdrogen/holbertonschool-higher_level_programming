#!/usr/bin/python3
""" doc
"""
import json


def save_to_json_file(my_obj, filename):
    """ fn to write from python to a file
    """
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
    f.close()
