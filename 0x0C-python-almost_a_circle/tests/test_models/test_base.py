#!/usr/bin/python3
"""Base.py unit tests"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square




class TestBase(unittest.TestCase):
    def test_id_none(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_id_specified(self):
        obj = Base(10)
        self.assertEqual(obj.id, 10)

     def setUp(self):
         Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        pass

    def test_A_nb_objects_private(self):
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_B_nb_objects_initialized(self):
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_C_instantiation(self):
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

    def test_D_constructor(self):
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_D_constructor_args_2(self):
        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)
        msg = "__init__() takes from 1 to 2 positional arguments but 3 \
were given"
        self.assertEqual(str(e.exception), msg)

    def test_E_consecutive_ids(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_F_id_synced(self):
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_F_id_synced_more(self):
        b = Base()
        b = Base("Foo")
        b = Base(98)
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_G_custom_id_int(self):
         i = 98
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_G_custom_id_str(self):
        i = "FooBar"
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_G_id_keyword(self):
        i = 421
        b = Base(id=i)
        self.assertEqual(b.id, i)

if __name__ == '__main__':
    unittest.main()
