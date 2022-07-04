from shopping_cart import ShoppingCart

class Customer:
    def __init__(self):
        self.name = ' '

    def run_app(self):
        self.customer_name()
        print(f'Hello, {self.name}. Have a great shopping!')
        while True:
            cart.run_shopping_cart()
            is_cart_empty = self.is_empty_cart()
            if is_cart_empty == True:
                continue
            else:
                break

    def customer_name(self):
        self.name = input('Enter your name: ')

    def is_empty_cart(self):
        user_input = input('(Yes) Do you want to continue to checkout?  (No) To empty your cart : ').lower()
        if user_input == 'n' or user_input == 'no':
            cart.empty_cart()
            self.empty_cart = True
            return self.empty_cart
        else:
            print('\nThanks for purchase. Please, come again!\n')

cart = ShoppingCart()
