class CoffeeMachine:
    def __init__(self):
        self.menu = dict()
        self.beans_stock = 100
        self.milk_stock = 100

    def add_coffee(self, coffee):
        self.menu[coffee.name] = coffee

    def restock_beans(self, quantity: int):
        self.beans_stock += quantity

    def restock_milk(self, quantity: int):
        self.milk_stock += quantity

    def show_stock(self):
        print(f"Beans stock = {self.beans_stock}")
        print(f"Milk stock = {self.milk_stock}")

    def show_menu(self):
        print("Menu:")
        print("".ljust(6), "Name".ljust(14), "Price")
        for i, item in enumerate(self.menu.items(), start = 1):
            print(f"{(str(i)+'.').ljust(6)} {item[1].name.ljust(15)}${item[1].price}")

    def check_beans_stock(self, coffee):
        if coffee in self.menu and self.menu[coffee].beans <= self.beans_stock:
            return True
        else:
            print("Not enough coffee beans, sliha!")
            return False

    def check_milk_stock(self, coffee):
        if coffee in self.menu and self.menu[coffee].milk <= self.milk_stock:
            return True
        else:
            print("Not enough milk, please choose another drink or ask the administrator for help")
            return False

    def stock_decrease_by_ordering(self, coffee_name):
        self.beans_stock -= self.menu[coffee_name].beans
        self.milk_stock -= self.menu[coffee_name].milk

    def choose_payment_method(self):
        print("Please choose payment method.")
        print("1. Cash")
        print("2. Card")
        while True:
            choose = input()
            if choose == "1" or choose.lower() == "cash":
                return True
            elif choose == "2" or choose.lower() == "card":
                return True
            else:
                print("Invalid input")

    def payment(self, coffee_name):
        while True:
            print(f"\nThe price of your coffe is {self.menu[coffee_name].price}")
            price = input("\nPlease make a payment, input price: ")
            if float(price) == float(self.menu[coffee_name].price):
                print("\nThanks for purchase. Please, wait until your coffee is ready")
                return True
            else:
                print("\nWrong sum! Try again")

    def choose_coffee(self):
        while True:
            coffee_name = input("\nEnter name of coffee you would like: ")
            coffee_name = coffee_name.capitalize()
            if coffee_name in self.menu:
                beans = self.check_beans_stock(coffee_name)
                milk = self.check_milk_stock(coffee_name)
                if beans and milk:
                    print("Nice choose!")
                    return coffee_name
                elif not beans:
                    print("Ask the administrator for help")
                    return False
            elif int(coffee_name) in list(range(1, len(self.menu) + 1)):
                for i, item in enumerate(self.menu, start=1):
                    if coffee_name == str(i):
                        beans = self.check_beans_stock(coffee_name)
                        milk = self.check_milk_stock(coffee_name)
                        if beans and milk:
                            print("Nice choose!")
                            return item
                        elif not beans:
                            print("Ask the administrator for help")
                            return False
            else:
                print("There is no such coffee yet. Please try again.")
