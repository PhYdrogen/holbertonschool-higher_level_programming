#!/usr/bin/python3
""" doc
"""


def append_write(filename="", text=""):
    """ append to a file fn
    """
    with open(filename, 'a', encoding="utf-8") as f:
        char_written = f.write(text)
    f.close()
    return char_written
