
class VegetableModel:
    def __init__(self, id, name, quantity=0, price=0,site=""):
        self.id = id
        self.name = name
        self.quantity = int(quantity)
        self.price = int(price)
        self.site = site


