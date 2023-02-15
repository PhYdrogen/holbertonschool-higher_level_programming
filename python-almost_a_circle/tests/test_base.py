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


if __name__ == '__main__':
    unittest.main()
