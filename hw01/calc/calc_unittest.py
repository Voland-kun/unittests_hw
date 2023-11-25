import unittest
import calc


class TestCalc(unittest.TestCase):
    def setUp(self):
        self.test_subject = calc.Calculator()

    def test_discount(self):
        self.assertEqual(100, self.test_subject.calculate_discount(100, 0))
        self.assertEqual(70, self.test_subject.calculate_discount(100, 30))
        self.assertRaises(ValueError, self.test_subject.calculate_discount, 100, 101)
        self.assertRaises(ValueError, self.test_subject.calculate_discount, -100, 30)
        self.assertRaises(ValueError, self.test_subject.calculate_discount, 100, -30)
        self.assertRaises(TypeError, self.test_subject.calculate_discount, 100, 'text')
        self.assertRaises(TypeError, self.test_subject.calculate_discount, 'text', 30)


if __name__ == '__main__':
    unittest.main()
