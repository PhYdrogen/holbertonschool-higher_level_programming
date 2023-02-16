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

    def test_rectangle_tp_dict(self):
        s6 = Rectangle(1, 2, 3, 4, 89).to_dictionary()
        self.assertEqual(type(s6), dict)

    def test_rectangle_update(self):
        s7 = Rectangle(1, 2, 3, 4, 5)
        s7.update(89)
        self.assertEqual(s7.id, 89)
        s7.update(89, 1)
        self.assertEqual(s7.width, 1)
        s7.update(89, 1, 2)
        self.assertEqual(s7.height, 2)
        s7.update(89, 1, 2, 3)
        self.assertEqual(s7.x, 3)
        s7.update(89, 1, 2, 3, 4)
        self.assertEqual(s7.y, 4)

    def test_rectangle_create(self):
        r8 = Rectangle.create(**{'id': 89})
        self.assertEqual(r8.id, 89)
        r8 = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r8.width, 1)
        r8 = Rectangle.create(**{'id': 89, 'width': 1, 'height':2})
        self.assertEqual(r8.height, 2)
        r8 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r8.x, 3)        
        r8 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r8.y, 4)
        
    def test_rectangle_save(self):
        #r9 = Rectangle(1, 2)
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
          self.assertEqual(file.read(), '[]')
        file.close()
      
        #self.assertEqual(Rectangle.save_to_file([]), None)
        #self.assertEqual(Rectangle.save_to_file([r9]), None)
       
if __name__ == '__main__':
    unittest.main()
