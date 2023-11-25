class Shop:
    def __init__(self):
        self.products = []

    def get_products(self):
        return self.products

    def set_products(self, products):
        self.products = products

    def get_sorted_list_products(self):
        return sorted(self.products, key=lambda x: x.get_cost(), reverse=True)

    def get_most_expensive_product(self):
        return max(self.products, key=lambda x: x.get_cost())
