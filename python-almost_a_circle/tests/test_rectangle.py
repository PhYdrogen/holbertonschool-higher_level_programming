#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_rectangle_1_string_2(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(1, "2")
        self.assertTrue('height must be an integer' in str(context.exception))

    def test_rectangle_1_0(self):
      with self.assertRaises(ValueError) as context:
        Rectangle(1, 0)
      self.assertTrue('height must be > 0' in str(context.exception))

    def test_rectangle_1_2(self):
        r2 = Rectangle(1, 2)
        self.assertEqual(r2.height, 2)

    def test_rectangle_1_2_3(self):
        r3 = Rectangle(1, 2, 3)
        self.assertEqual(r3.x, 3)

    def test_rectangle_1_2_3_4(self):
        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r3.y, 4)

    def test_area(self):
        r4 = Rectangle(1, 1)
        self.assertEqual(r4.area(), 1)

    def test_str(self):
        r5 = Rectangle(1, 1)
        self.assertEqual("{}".format(r5), "[Rectangle] ({}) 0/0 - 1/1".format(r5.id)) 

    def test_square_tp_dict(self):
        s6 = Square(1, 2, 3)
        self.assertEqual(type(s6.to_dictionary()), dict)

if __name__ == '__main__':
    unittest.main()
