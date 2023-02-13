#!/usr/bin/python3
""" doc for file """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class square herit from rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)
