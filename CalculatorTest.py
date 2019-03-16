from unittest import TestCase

from Calculator import Calculator

class CalculatorTest(TestCase):
    def test_add(self):
        self.assertEqual(Calculator().add(""), 0, "Empty string")

    def test_add_string(self):
        self.assertEqual(Calculator().add("1"), 1, "One number")

    def test_add_stringWithNumber(self):
        self.assertEqual(Calculator().add("1"), 1, "One number")
        self.assertEqual(Calculator().add("2"), 2, "One number")
