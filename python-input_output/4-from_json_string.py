#!/usr/bin/python3
""" doc
"""
import json


def from_json_string(my_str):
    """ take a string put it to json
    """
    return json.loads(my_str)
