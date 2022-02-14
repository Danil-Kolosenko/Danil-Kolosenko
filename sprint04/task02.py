class Pizza:
    order_number = 0

    def __init__(self, ingredients):
        Pizza.order_number += 1
        self.ingredients = ingredients
        self.order_number = Pizza.order_number


    @classmethod
    def hawaiian(cls):
        return cls(["ham", "pineapple"])

    @classmethod
    def meat_festival(cls):
        return cls(["beef", "meatball", "bacon"])

    @classmethod
    def garden_feast(cls):
        return cls(["spinach", "olives", "mushroom"])
