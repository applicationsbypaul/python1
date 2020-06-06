"""
Program: test_average_scores.py
Author: Paul Ford
Last date modified: 06/6/2020
The purpose of this program is to say
Hello World.
"""
import unittest

from TOP2.format_output.average_scores import average


class MyTestCase(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average(), 90)


if __name__ == '__main__':
    unittest.main()

#test
#input          #expected           #results

