#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_base_assign_id_auto_0(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_base_assign_id_auto_1(self):
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_base_assign_id_auto_2(self):
        b3 = Base(89)
        self.assertEqual(b3.id, 89)


if __name__ == '__main__':
    unittest.main()
