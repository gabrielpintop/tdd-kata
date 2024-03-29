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

    def test_add_stringWithTwoNumbers(self):
        self.assertEqual(Calculator().add("1,3"), 4, "Two numbers")

    def test_add_stringWithMultipleNumbers(self):
        self.assertEqual(Calculator().add("5,2,4,1"), 12, "Multiple numbers")

    def test_add_stringWithMultipleNumbersAndSeparators(self):
        self.assertEqual(Calculator().add("5,2&4:1:2&8"), 22, "Multiple numbers with different separators")