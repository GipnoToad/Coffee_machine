from administrator import Administrator
from coffee_machine import CoffeeMachine
from coffee import Coffee
import time


class Main:
    coffee_machine = CoffeeMachine()
    admin = Administrator(coffee_machine)

    espresso = Coffee("Espresso", 2.5, 20, 0)
    latte = Coffee("Latte", 3.5, 15, 10)
    americano = Coffee("Americano", 5.5, 18, 15)

    admin.add_coffee(espresso)
    admin.add_coffee(latte)
    admin.add_coffee(americano)

    def show_operations(self):
        print("\nYou have different options to choose:")
        print("1 - Show menu.")
        print("2 - Access admin panel.")
        while True:
            choose = input()
            if choose == "1":
                return "1"
            elif choose == "2":
                return "2"
            else:
                print("\nWrong input, tyr again")

    def admin_operations(self):
        print("\nYou have different options to choose:")
        print("1 - Add coffee.")
        print("2 - Delete coffee.")
        print("3 - Look stock of supplies.")
        print("4 - Restock beans.")
        print("5 - Restock milk.")
        print("x - Exit")
        while True:
            choose = input()
            if choose == "1":
                return "1"
            elif choose == "2":
                return "2"
            if choose == "3":
                return "3"
            elif choose == "4":
                return "4"
            if choose == "5":
                return "5"
            elif choose.lower() == "x":
                return "x"
            else:
                print("\nWrong input, tyr again")

    def add_new_coffee_check(self):
        try:
            while True:
                name = str(input("\nInput name of new coffee: "))
                price = float(input("Price in $: "))
                beans = int(input("quantity of beans spending: "))
                milk = int(input("quantity of milk spending: "))
                return name.capitalize(), price, beans, milk
        except Exception as e:
            print(f"Some exception appears: {e}")

    def run(self):
        print("\nGreetings!")
        choose = self.show_operations()
        if choose == "1":
            print("Now you can choose your coffee!")
            self.coffee_machine.show_menu()
            coffee_name = self.coffee_machine.choose_coffee()
            if coffee_name:
                if self.coffee_machine.choose_payment_method():
                    if self.coffee_machine.payment(coffee_name):
                        self.coffee_machine.stock_decrease_by_ordering(coffee_name)
                time.sleep(5)
                print("\nYour coffee is ready!")
                print("\nThank you. Come again!")
                time.sleep(2)
                self.run()
            else:
                print("\nSorry, no supplies in stock. Ask for administrator.")
                self.run()
        elif choose == "2":
            if self.admin.login():
                while True:
                    admin_choose = self.admin_operations()
                    if admin_choose == "1":
                        coffee = Coffee(*self.add_new_coffee_check())
                        self.admin.add_coffee(coffee)
                    elif admin_choose == "2":
                        self.admin.delete_coffee()
                    elif admin_choose == "3":
                        self.admin.show_stock()
                    elif admin_choose == "4":
                        self.admin.restock_beans()
                    elif admin_choose == "5":
                        self.admin.restock_milk()
                    elif admin_choose == "x":
                        self.run()
            else:
                print("Access denied")
                self.run()


main = Main()
main.run()

