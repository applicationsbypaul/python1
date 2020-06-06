import unittest
from unittest import mock
from MOD3.format_output.average_scores import average


class MyTestCase(unittest.TestCase):

    def test_average(self):
        with mock.patch('builtins.input', side_effect=[85, 90, 95]):
            assert average() == 90


if __name__ == "__main__":
    unittest.main()
