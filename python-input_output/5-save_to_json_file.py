#!/usr/bin/python3
""" doc
"""
import json


def save_to_json_file(my_obj, filename):
    """ create a new file
    """
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
    f.close()
