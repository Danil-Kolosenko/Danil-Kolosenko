class Goods:

    def __init__(self, price, discount_strategy=None):
        self.price = price
        self.discount_strategy = discount_strategy
        self.price_after_discount()

    def price_after_discount(self):
        if self.discount_strategy == twenty_percent_discount:
            return twenty_percent_discount(self.price)
        elif self.discount_strategy == on_sale_discount:
            return on_sale_discount(self.price)
        else:
            return self.price

    def __repr__(self):
        return f"Price: {self.price}, price after discount: {self.price_after_discount()}"

def on_sale_discount(order):
    return order * 0.5

def twenty_percent_discount(order):
    return order * 0.8
