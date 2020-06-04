import unittest
from main.camper_age_input import convert_to_months


class MyTestCase(unittest.TestCase):
    def test_convert_to_months(self):
        self.assertEqual(convert_to_months(5), 60)


if __name__ == '__main__':
    unittest.main()
