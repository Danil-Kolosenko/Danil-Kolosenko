import unittest

class Product:
    def __init__(self, name, prise, count):
        self.name = name
        self.prise = prise
        self.count = count


class Cart:
    def __init__(self, pr_list):
        self.pr_list = pr_list
        self.sum_price = 0


    def get_total_price(self):
        for product in self.pr_list:
            if product.count > 20:
                self.sum_price += (product.count * product.prise) * 0.5
            elif product.count == 20:
                self.sum_price += (product.count * product.prise) * 0.7
            elif product.count >= 10:
                self.sum_price += (product.count * product.prise) * 0.8
            elif product.count >= 7:
                self.sum_price += (product.count * product.prise) * 0.9
            elif product.count >= 5:
                self.sum_price += (product.count * product.prise) * 0.95
            else:
                self.sum_price += (product.count * product.prise)

        return self.sum_price

class CartTest(unittest.TestCase):
    def test_t1(self):
        self.assertEqual(1,1)
