#!/usr/bin/python3
import unittest
from models.square import Square
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

class TestSquare(unittest.TestCase):
    def test_init(self):
        s = Square(10, 5, 10, 1)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 10)
        self.assertEqual(s.id, 1)

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_str(self):
        s = Square(10, 5, 10, 1)
        self.assertEqual(str(s), "[Square] (1) 5/10 - 10")

    def test_display(self):
        s = Square(3, 2, 1)
        expected_output = "\n  ###\n  ###\n  ###\n"
        with captured_output() as (out, err):
            s.display()
        self.assertEqual(out.getvalue(), expected_output)

    def test_update(self):
        s = Square(5)
        s.update(1, 10, 5, 10)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 10)
        self.assertEqual(s.id, 1)

    def test_to_dictionary(self):
        s = Square(10, 5, 10, 1)
        expected_dict = {'id': 1, 'size': 10, 'x': 5, 'y': 10}
        self.assertEqual(s.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
