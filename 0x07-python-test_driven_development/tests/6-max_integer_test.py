#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3, -2]), -1)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 5, 0, 2]), 5)
        self.assertEqual(max_integer([-1, -5, 0, -2]), 0)

    def test_single_element_list(self):
        self.assertEqual(max_integer([42]), 42)

    def test_large_numbers(self):
        self.assertEqual(max_integer([1000, 10000, 100000]), 100000)

    def test_zero(self):
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_float_numbers(self):
        self.assertEqual(max_integer([2.5, 1.2, 3.8, 0.7]), 3.8)

    def test_mixed_float_int(self):
        self.assertEqual(max_integer([2, 5.5, 7, 3.2]), 7)

    def test_mixed_negative_float(self):
        self.assertEqual(max_integer([-2.5, -1.2, -3.8, -0.7]), -0.7)

    def test_ints_and_floats(self):
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

if __name__ == '__main__':
    unittest.main()
