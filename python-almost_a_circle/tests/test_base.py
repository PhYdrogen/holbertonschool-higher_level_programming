#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_base_1(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        
    def test_base_2(self):
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_base_3(self):
        b3 = Base(89)
        self.assertEqual(b3.id, 89)

    def test_base_4(self):
        b4 = Base.to_json_string(None)
        self.assertEqual(b4, '[]')

    def test_base_5(self):
        b5 = Base.to_json_string([])
        self.assertEqual(b5, "[]")

     def test_base_6(self):
        b6 = Base.to_json_string([{'id': 12}])
        self.assertEqual(b6, '[{"id": 12}]')

    def test_base_7(self):
        b7 = Base.from_json_string(None)
        self.assertEqual(b7, [])

    def test_base_8(self):
        b8 = Base.from_json_string("[]")
        self.assertEqual(b8, [])
        
    def test_base_9(self):
        b9 = Base.from_json_string('[{ "id":89 }]')
        self.assertEqual(b9, [{'id': 89}])


if __name__ == '__main__':
    unittest.main()
