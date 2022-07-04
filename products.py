# As a developer, I want the Product class to have class properties to keep track of the Product’s name, price, and category.
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = float(price)
        self.category = category

    
