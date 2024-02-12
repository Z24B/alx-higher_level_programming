#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from io import StringIO
from contextlib import contextmanager
import sys

@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class TestRectangle(unittest.TestCase):
    def test_init(self):
        r = Rectangle(10, 20, 5, 10, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 10)
        self.assertEqual(r.id, 1)

    def test_area(self):
        r = Rectangle(5, 5)
        self.assertEqual(r.area(), 25)

    def test_str(self):
        r = Rectangle(10, 20, 5, 10, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 5/10 - 10/20")

    def test_display(self):
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with captured_output() as (out, err):
            r.display()
        self.assertEqual(out.getvalue(), expected_output)

    def test_update(self):
        r = Rectangle(5, 5)
        r.update(1, 10, 20, 5, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 10)
        self.assertEqual(r.id, 1)

    def test_to_dictionary(self):
        r = Rectangle(10, 20, 5, 10, 1)
        expected_dict = {'id': 1, 'width': 10, 'height': 20, 'x': 5, 'y': 10}
        self.assertEqual(r.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
