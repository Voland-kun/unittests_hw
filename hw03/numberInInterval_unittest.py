import unittest
from numberInInterval import number_interval


class TestNumberInterval(unittest.TestCase):
    def test_number_interval(self):
        self.assertTrue(number_interval(50))
        self.assertFalse(number_interval(25))
        self.assertFalse(number_interval(100))


if __name__ == '__main__':
    unittest.main()
