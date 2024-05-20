class Meal:

    def __init__(self, dish, price, is_available=False):
        if dish == " ":
            raise Exception("Dish cannot be an empty string!")
        elif price == " ":
            raise Exception("Price cannot be an empty string!")
        self.dish = dish
        self.price = price
        self.is_available = is_available
        


    def mark_available(self):
        self.is_available = True