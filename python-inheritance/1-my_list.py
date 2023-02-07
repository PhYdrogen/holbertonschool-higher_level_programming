#!/usr/bin/python3
""" Class MyList
"""


class MyList(list):
    """ Doc for my class
    """
    def print_sorted(self):
        copy_list = self[:]
        print(sorted(copy_list))
