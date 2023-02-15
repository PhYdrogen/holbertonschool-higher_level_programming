#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_basic(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.id, 3)


if __name__ == '__main__':
    unittest.main()
