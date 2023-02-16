#!/usr/bin/python3
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_square_1(self):
        s1 = Square(1)
        self.assertEqual(s1.size, 1)

    def test_square_1_2(self):
        s2 = Square(1, 2)
        self.assertEqual(s2.x, 2)

    def test_square_1_2_3(self):
        s3 = Square(1, 2, 3)
        self.assertEqual(s3.y, 3)

    def test_square_1_string(self):
        with self.assertRaises(TypeError) as context:
            Square("1")
        self.assertTrue('width must be an integer' in str(context.exception))

    def test_square_1_2_string(self):
        with self.assertRaises(TypeError) as context:
            Square(1, "2")
        self.assertTrue('x must be an integer' in str(context.exception))

    def test_square_1_2_3_string(self):
        with self.assertRaises(TypeError) as context:
            Square(1, 2, "3")
        self.assertTrue('y must be an integer' in str(context.exception))

    def test_square_1_2_3_4(self):
        s4 = Square(1, 2, 3, 4)
        self.assertEqual(s4.id, 4)

    def test_square_negative_1(self):
        with self.assertRaises(ValueError) as context:
            Square(-1)
        self.assertTrue('width must be > 0' in str(context.exception))

    def test_square_negative_2(self):
        with self.assertRaises(ValueError) as context:
            Square(1, -2)
        self.assertTrue('x must be >= 0' in str(context.exception))

    def test_square_negative_3(self):
        with self.assertRaises(ValueError) as context:
            Square(1, 2, -3)
        self.assertTrue('y must be >= 0' in str(context.exception))

    def test_square_negative_0(self):
        with self.assertRaises(ValueError) as context:
            Square(0)
        self.assertTrue('width must be > 0' in str(context.exception))

    def test_square_update(self):
        s7 = Square(1, 2, 3)
        s7.update(89)
        self.assertEqual(s7.id, 89)
        s7.update(89, 1)
        self.assertEqual(s7.size, 1)
        s7.update(89, 1, 2)
        self.assertEqual(s7.x, 2)
        s7.update(89, 1, 2, 3)
        self.assertEqual(s7.y, 3)

if __name__ == '__main__':
    unittest.main()
