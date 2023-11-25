import unittest

from product import Product
from shop import Shop


class ShopTest(unittest.TestCase):
    def setUp(self):
        self.prod1 = Product("prod1", 5)
        self.prod2 = Product("prod2", 10)
        self.prod3 = Product("prod3", 1)
        self.test_subject = Shop()
        self.test_subject.set_products([self.prod1, self.prod2, self.prod3])

    def test_get_sorted_list_products(self):
        sorted_products = self.test_subject.get_sorted_list_products()
        self.assertEqual(sorted_products, [self.prod2, self.prod1, self.prod3])

    def test_get_most_expensive_product(self):
        self.assertEqual(self.test_subject.get_most_expensive_product(), self.prod2)
