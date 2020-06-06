"""
Program: test_average_scores.py
Author: Paul Ford
Last date modified: 06/6/2020
Test average method
"""
import unittest

from TOP2.format_output.average_scores import average


class MyTestCase(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average(), 2.0)


if __name__ == '__main__':
    unittest.main()

# test results
# input          #expected           #results
# 90 95 100        95.00               95.00
# 44 96 77         72.33         failed it was correct number maybe test needs decimal precision
# 1 2 3             2                   2.0
