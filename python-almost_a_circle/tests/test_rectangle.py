#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_basic(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.id, 3)

    def test_basic_three(self):
        r2 = Rectangle(1, 2, 3)
        self.assertEqual(r2.id, 5)

    def test_basic_four(self):
        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r3.id, 4)
