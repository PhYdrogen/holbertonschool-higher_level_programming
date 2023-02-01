#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Doc for Unittest
    """

    def maxatend(self):
        """Test if last is max
        """
        test = [1, 2, 3]
        self.assertEqual(max_integer(test), 3)


if __name__ == '__main__':
    unittest.main()
