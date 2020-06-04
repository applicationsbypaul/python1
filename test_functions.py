import unittest
from main import camper_age_input


def convert_to_months(x):
    pass


class MyTestCase(unittest.TestCase):
    def test_convert_to_months(self):
        self.assertEqual(convert_to_months(3), 60)


if __name__ == '__main__':
    unittest.main()
