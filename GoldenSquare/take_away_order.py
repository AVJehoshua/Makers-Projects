class Order:

    def __init__(self):
        self.list_menu = []
        self.in_stock = []


    def add(self, dish):
        self.list_menu.append(dish)

    def list_all(self):
        return self.list_menu
    
    def available_dishes(self):
        for dish in self.list_menu:
            if dish.is_available == True:
                self.in_stock.append(dish)
        return self.in_stock
