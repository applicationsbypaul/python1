"""
Program: Test_functions
Author: Paul Ford
Last date modified: 06/3/2020

Testing the method from the main convert to months
"""
import unittest
from camper_age_input import convert_to_months


class MyTestCase(unittest.TestCase):
    def test_convert_to_months(self):
        self.assertEqual(convert_to_months(5), 60)

    def test_convert_to_months1(self):
        self.assertEqual(convert_to_months(4), 48)


if __name__ == '__main__':
    unittest.main()