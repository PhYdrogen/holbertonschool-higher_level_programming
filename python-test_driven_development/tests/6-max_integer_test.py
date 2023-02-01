#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest


def max_integer(list=[]):
    """Doc
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result


class TestMaxInteger(unittest.TestCase):
    """Doc for Unittest
    """

    def test_maxatend(self):
        """Test if last is max
        """
        test = [1, 2, 3]
        self.assertEqual(max_integer(test), 3)


if __name__ == '__main__':
    unittest.main()
