from products import Product


class ShoppingCart:
    def __init__(self):
        self.customer_name = str
        self.shopping_cart = []
        self.total_price = 0
        self.is_checkout = False
        self.beverages_list = [Product('Red Bull 12oz', 5.49, 'Beverages'), Product('Red Bull 8oz', 3.49, 'Beverages'), Product('Coke', 1.49, 'Beverages'), Product('Sprite', 1.49, 'Beverages'), Product('Fanta Orange', 1.49, 'Beverages')]
        self.fruits_list = [Product('Apple', 1.69, 'Fruits'), Product('Orange', 1.99, 'Fruits'), Product('Banana', 1.89, 'Fruits'), Product('Peach', 2.49, 'Fruits'), Product('Strawberry', 1.79, 'Fruits')]
        self.dairy_list = [Product('YoNan', 1.49, 'Dairy'), Product('Maizy', 1.59, 'Dairy'), Product('Amazicana', 2.59, 'Dairy'), Product('For Coffy Made', 2.89, 'Dairy'), Product('Organic Eggs', 3.99, 'Dairy')]


    def run_shopping_cart(self):
        self.is_checkout = self.add_product()
        if self.is_checkout == True:
            self.total_price = self.calculate_total_price()
            index = 0
            print('Your shopping cart contains:\n')
            for item in self.shopping_cart:
                item = (f'${self.shopping_cart[index].price} --- {self.shopping_cart[index].name}')
                print(item)
                index += 1
            print(f'\nTOTAL: ${round(self.total_price, 2)}\n')

    def add_product(self):
        self.category_choice = self.choose_category()
        while self.category_choice != 0:
            if self.category_choice == 1:
                self.list_length = len(self.beverages_list)
                self.display_beverage()
                self.number_selected = self.get_beverage()
                if self.number_selected == self.list_length + 1:
                    self.add_product()
                    if self.category_choice == 0:
                        self.is_checkout = True
                        return self.is_checkout
                else:
                    continue
            if self.category_choice == 2:
                self.list_length = len(self.fruits_list)
                self.display_fruits()
                self.number_selected = self.get_fruits()
                if self.number_selected == self.list_length + 1:
                    self.add_product()
                    if self.category_choice == 0:
                        self.is_checkout = True
                        return self.is_checkout
                else:
                    continue          
            if self.category_choice == 3:
                self.list_length = len(self.dairy_list)
                self.display_dairy()
                self.number_selected = self.get_dairy()
                if self.number_selected == self.list_length + 1:
                    self.add_product()
                    if self.category_choice == 0:
                        self.is_checkout = True
                        return self.is_checkout
                else:
                    continue    

    def display_beverage(self):
        num = 1
        for self.item in self.beverages_list:
            print(f'{num}. {self.beverages_list[num - 1].name}   ${self.beverages_list[num -1].price}')
            num += 1
        self.back_to_categories()
  
    def display_fruits(self):
        num = 1
        for self.item in self.fruits_list:
            print(f'{num}. {self.fruits_list[num - 1].name}   ${self.fruits_list[num -1].price} /lb')
            num += 1
        self.back_to_categories()

    def display_dairy(self):
        num = 1
        for self.item in self.dairy_list:
            print(f'{num}. {self.dairy_list[num - 1].name}   ${self.dairy_list[num -1].price}')
            num += 1
        self.back_to_categories()

    def choose_category(self):
        print('\nAvailable categories:\n1. Beverages\n2. Fruits\n3. Dairy\n\n0. Checkout\n')
        category_choice = int(input('Please, choose category: '))
        return category_choice
    
    def get_beverage(self):
        number_selected = int(input('Select number: '))
        if number_selected != self.list_length + 1 and number_selected <= self.list_length:
            self.shopping_cart.append(self.beverages_list[number_selected - 1])
        return number_selected
    
    def get_fruits(self):
        number_selected = int(input('Select number: '))
        if number_selected != self.list_length + 1 and number_selected <= self.list_length:
            self.shopping_cart.append(self.fruits_list[number_selected - 1])
        return number_selected
    
    def get_dairy(self):
        number_selected = int(input('Select number: '))
        if number_selected != self.list_length + 1 and number_selected <= self.list_length:
            self.shopping_cart.append(self.dairy_list[number_selected - 1])
        return number_selected
    
    def back_to_categories(self):
        print(f'\n{self.list_length + 1}. Back to categories.\n')
    
    def calculate_total_price(self):
        index = 0
        for product in self.shopping_cart:
            self.total_price = self.total_price + self.shopping_cart[index].price
            index += 1
        return self.total_price
    
    def empty_cart(self):
        self.shopping_cart.clear()