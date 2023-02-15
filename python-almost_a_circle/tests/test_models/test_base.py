#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def setUp(self):
        self.base = Base()

    def test_base_assign_id_auto_0(self):
        self.assertEqual(self.base.id, 1)

    def test_base_assign_id_auto_1(self):
        self.assertEqual(self.base.id, 2)

    def test_base_assign_id_auto_2(self):
        b3 = Base(89)
        self.assertEqual(b3.id, 89)

    def test_base_to_json_none(self):
        b4 = Base.to_json_string(None)
        self.assertEqual(b4, '[]')

    def test_base_to_json_empty(self):
        b5 = Base.to_json_string([])
        self.assertEqual(b5, "[]")

    def test_base_to_json_id_12(self):
        b6 = Base.to_json_string([{'id': 12}])
        self.assertEqual(b6, '[{"id": 12}]')

    def test_base_from_json_none(self):
        b7 = Base.from_json_string(None)
        self.assertEqual(b7, [])

    def test_base_from_json_empty(self):
        b8 = Base.from_json_string("[]")
        self.assertEqual(b8, [])

    def test_base_from_json_id_89(self):
        b9 = Base.from_json_string('[{ "id":89 }]')
        self.assertEqual(b9, [{'id': 89}])


if __name__ == '__main__':
    unittest.main()
