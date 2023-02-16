#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    def test_rectangle_1(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(1)
        self.assertTrue("Rectangle.__init__() missing \
                        1 required positional argument: 'height'"
                        in str(context.exception))

    def test_rectangle_1_2(self):
        r2 = Rectangle(1, 2)
        self.assertEqual(r2.height, 2)

    def test_rectangle_1_2_3(self):
        r3 = Rectangle(1, 2, 3)
        self.assertEqual(r3.x, 3)

    def test_rectangle_1_2_3_4(self):
        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r3.y, 4)


if __name__ == '__main__':
    unittest.main()
