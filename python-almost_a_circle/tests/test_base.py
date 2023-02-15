#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square


class TestBase(unittest.TestCase):
    def test_base_assign_id_auto_0(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(89)
        self.assertEqual(b3.id, 89)

        b4 = Base.to_json_string(None)
        self.assertEqual(b4, '[]')

        b5 = Base.to_json_string([])
        self.assertEqual(b5, "[]")

        b6 = Base.to_json_string([{'id': 12}])
        self.assertEqual(b6, '[{"id": 12}]')

        b7 = Base.from_json_string(None)
        self.assertEqual(b7, [])

        b8 = Base.from_json_string("[]")
        self.assertEqual(b8, [])

        b9 = Base.from_json_string('[{ "id":89 }]')
        self.assertEqual(b9, [{'id': 89}])


class TestSquare(unittest.TestCase):

    def test_square_1(self):
        s1 = Square(1)
        self.assertEqual(s1.id, 3)
        s2 = Square(1, 2)
        self.assertEqual(s2.id, 4)
        s3 = Square(1, 2, 3)
        self.assertEqual(s3.id, 5)
        s4 = Square(1, 2, 3, 4)
        self.assertEqual(s4.id, 4)

    def test_square_4(self):
        with self.assertRaises(TypeError) as context:
            Square("1")
        self.assertTrue('width must be an integer' in str(context.exception))

        with self.assertRaises(TypeError) as context:
            Square(1, "2")
        self.assertTrue('x must be an integer' in str(context.exception))

        with self.assertRaises(TypeError) as context:
            Square(1, 2, "3")
        self.assertTrue('y must be an integer' in str(context.exception))

        with self.assertRaises(ValueError) as context:
            Square(-1)
        self.assertTrue('width must be > 0' in str(context.exception))

        with self.assertRaises(ValueError) as context:
            Square(1, -2)
        self.assertTrue('x must be >= 0' in str(context.exception))

        with self.assertRaises(ValueError) as context:
            Square(1, 2, -3)
        self.assertTrue('y must be >= 0' in str(context.exception))

        with self.assertRaises(ValueError) as context:
            Square(0)
        self.assertTrue('width must be > 0' in str(context.exception))

    def test_square_12(self):
        s5 = Square(1, 2, 3)
        self.assertEqual(s5.__str__(), "[Square] (6) 2/3 - 1")
        s6 = Square(1, 2, 3)
        self.assertEqual(s6.to_dictionary(),
                         {'id': 7, 'size': 1, 'x': 2, 'y': 3})
        s7 = Square(10, 20, 30)
        s7.update()
        self.assertEqual(s7.to_dictionary(),
                         {'id': 8, 'size': 10, 'x': 20, 'y': 30})
        s8 = Square(10, 20, 30)
        s8.update(89)
        self.assertEqual(s8.to_dictionary(),
                         {'id': 89, 'size': 10, 'x': 20, 'y': 30})
        s9 = Square(10, 20, 30)
        s9.update(89, 1)
        self.assertEqual(s9.to_dictionary(),
                         {'id': 89, 'size': 1, 'x': 20, 'y': 30})
        s10 = Square(10, 20, 30)
        s10.update(89, 1, 2)
        self.assertEqual(s10.to_dictionary(),
                         {'id': 89, 'size': 1, 'x': 2, 'y': 30})
        s11 = Square(10, 20, 30)
        s11.update(89, 1, 2, 3)
        self.assertEqual(s11.to_dictionary(),
                         {'id': 89, 'size': 1, 'x': 2, 'y': 3})
        s12 = Square(10, 20, 30)
        s12.update(**{'id': 89})
        self.assertEqual(s12.to_dictionary(),
                         {'id': 89, 'size': 10, 'x': 20, 'y': 30})
        s13 = Square(10, 20, 30)
        s13.update(**{'id': 89, 'size': 1})
        self.assertEqual(s13.to_dictionary(),
                         {'id': 89, 'size': 1, 'x': 20, 'y': 30})
        s14 = Square(10, 20, 30)
        s14.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s14.to_dictionary(),
                         {'id': 89, 'size': 1, 'x': 2, 'y': 30})
        s15 = Square(10, 20, 30)
        s15.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s15.to_dictionary(),
                         {'id': 89, 'size': 1, 'x': 2, 'y': 3})

    def test_square_22(self):
        with self.assertRaises(TypeError) as context:
            Square().create(**{'id': 89})
        self.assertTrue(
            "Square.__init__() missing 1 required positional argument: 'size'"
            in str(context.exception))

    def test_square_23(self):
        with self.assertRaises(TypeError) as context:
            Square().create(**{'id': 89, 'size': 1})
        self.assertTrue(
            "Square.__init__() missing 1 required positional argument: 'size'"
            in str(context.exception))

    def test_square_24(self):
        s16 = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s16.to_dictionary(),
                         {'id': 89, 'size': 1, 'x': 2, 'y': 0})

    def test_square_25(self):
        s17 = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s17.to_dictionary(),
                         {'id': 89, 'size': 1, 'x': 2, 'y': 3})
        """ test_square_save_json """
        self.assertEqual(s17.save_to_file(None), None)
        self.assertEqual(s17.save_to_file([]), None)
        self.assertEqual(s17.save_to_file([Square(1)]), None)


if __name__ == '__main__':
    unittest.main()
