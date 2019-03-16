from unittest import TestCase

from Calculator import Calculator

class CalculatorTest(TestCase):
    def test_add(self):
        self.assertEqual(Calculator().add(""), 0, "Empty string")
