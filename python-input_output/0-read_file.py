#!/usr/bin/python3
""" doc
"""


def read_file(filename=""):
    """ read_file fn
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
    print(read_data)
    f.close()
