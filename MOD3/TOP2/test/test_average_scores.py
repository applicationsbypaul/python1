import unittest
from unittest import mock
from TOP2.format_output.average_scores import average


def test_average():
    with mock.patch('builtins.input', side_effect=[85, 90, 95]):
        assert average() == 90


if __name__ == '__main__':
    test_average()
