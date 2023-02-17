#!/usr/bin/python3
import unittest
import os
from models.square import Square


class TestSquare(unittest.TestCase):
    @classmethod
    def tearDown(self):
        if os.path.exists("./Rectangle.json"):
            os.remove("Rectangle.json")
          
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

    def test_square_tp_dict(self):
        s6 = Square(1, 2, 3)
        self.assertEqual(type(s6.to_dictionary()), dict)
      
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
      
    def test_square_create(self):
        s8 = Square.create(**{'id': 89})
        self.assertEqual(s8.id, 89)
        s8 = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s8.size, 1)
        s8 = Square.create(**{'id': 89, 'size': 1, 'x': 3})
        self.assertEqual(s8.x, 3)        
        s8 = Square.create(**{'id': 89, 'size': 1, 'x': 3, 'y': 4})
        self.assertEqual(s8.y, 4)

    def test_str(self):
        s9 = Square(1)
        self.assertEqual("{}".format(s9), "[Square] ({}) 0/0 - 1".format(s9.id))

    def test_rectangle_save(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
          self.assertEqual(file.read(), '[]')
        file.close()
    
    def test_rectangle_save_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
          self.assertEqual(file.read(), "[]")
        file.close()
      
    def test_square_save_square(self):
        s10 = Square(1, 0, 0, 13)
        Square.save_to_file([s10])
        with open("Square.json", "r") as file:
          self.assertEqual(file.read(), '[{"id": 13, "size": 1, "x": 0, "y": 0}]')
        file.close()

    def test_load_square(self):
        Square.load_from_file()

if __name__ == '__main__':
    unittest.main()
