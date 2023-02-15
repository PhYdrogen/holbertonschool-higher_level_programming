#!/usr/bin/python3
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_square_1(self):
        s1 = Square(1)
        self.assertEqual(s1.id, 6)

    def test_square_1_2(self):
        s2 = Square(1, 2)
        self.assertEqual(s2.id, 7)

    def test_square_1_2_3(self):
        s3 = Square(1, 2, 3)
        self.assertEqual(s3.id, 8)

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


if __name__ == '__main__':
    unittest.main()
