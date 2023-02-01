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
        test1 = [1, 2, 3]
        self.assertEqual(max_integer(test1), 3)

    def test_maxatfront(self):
        """Test
        """
        test2 = [3, 2, 0]
        self.assertEqual(max_integer(test2), 3)

    def test_maxatmid(self):
        """Test
        """
        test3 = [1, 3, 2]
        self.assertEqual(max_integer(test3), 3)

    def test_one_negative(self):
        """Test
        """
        test4 = [-1, 3, 2]
        self.assertEqual(max_integer(test4), 3)

    def test_only_negative(self):
        """Test
        """
        test5 = [-1, -3, -2]
        self.assertEqual(max_integer(test5), -1)

    def test_one_elem(self):
        """Test
        """
        test6 = [3]
        self.assertEqual(max_integer(test6), 3)

    def test_list_empty(self):
        """Test
        """
        test7 = []
        self.assertEqual(max_integer(test7), None)


if __name__ == '__main__':
    unittest.main()
