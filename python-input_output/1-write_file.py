#!/usr/bin/python3
""" doc
"""


def write_file(filename="", text=""):
    """ write_file fn
    """
    with open(filename, encoding="utf-8") as f:
        f.write(text)
    f.close()
