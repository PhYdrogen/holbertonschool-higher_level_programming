#!/usr/bin/python3
""" doc
"""


def write_file(filename="", text=""):
    """ write_file fn
    """
    with open(filename, "w", encoding="utf-8") as f:
        char_written = f.write(text)
    f.close()
    return char_written
