#!/usr/bin/python3
""" doc
"""
import json


def load_from_json_file(filename):
    """ fn to load from file and translate to obj
    """
    with open(filename, 'r') as f:
        read_data = f.read()
    f.close()
    return json.dumps(read_data)
