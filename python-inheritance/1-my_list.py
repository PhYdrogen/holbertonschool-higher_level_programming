#!/usr/bin/python3
""" Class MyList
"""


class MyList(list):
    """ Doc for my class
    """
    def print_sorted(self):
        copy_list = self[:]
        if len(copy_list) == 0:
            return []
        print(sorted(copy_list))
