import unittest
from unittest import mock

from TOP2.format_output.average_scores import average


class MyTestCase(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average(), 90)


if __name__ == '__main__':
    unittest.main()
