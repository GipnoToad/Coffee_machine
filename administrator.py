class Administrator:
    def __init__(self, coffee_machine):
        self.admin = coffee_machine
        self._login = "admin"
        self._password = "admin"

    @property
    def lp(self):
        return self._login, self._password

    def add_coffee(self, coffee):
        self.admin.add_coffee(coffee)
        print(f"{coffee.name} added to the menu.")

    def delete_coffee(self):
        try:
            while True:
                coffee_name = input("Please, input name of the coffee to delete: ").capitalize()
                if coffee_name in self.admin.menu:
                    del self.admin.menu[coffee_name]
                    print(f"{coffee_name} was deleted from the menu.")
                    break
                else:
                    print("There is no such coffee.")
        except ValueError as e:
            print(f"ValueError appears: {e}")

    def restock_beans(self):
        try:
            while True:
                quantity = int(input("Input quantity of beans to add to machine: "))
                self.admin.restock_beans(quantity)
                print(f"Now quantity of beans is: {self.admin.beans_stock}")
                break
        except Exception as e:
            print(f"Exception appears: {e}")

    def restock_milk(self):
        try:
            while True:
                quantity = int(input("Input quantity of milk to add to machine: "))
                self.admin.restock_milk(quantity)
                print(f"Now quantity of milk is: {self.admin.milk_stock}")
                break
        except Exception as e:
            print(f"Exception appears: {e}")

    def show_stock(self):
        self.admin.show_stock()

    def login(self):
        while True:
            login = input("\nPlease input login: ")
            password = input("\nPlease input password: ")
            if login == self._login and password == self._password:
                print("\nLog in successful!")
                return True
            elif login != self._login:
                print("\nWrong login, try again")
            elif password != self._password:
                print("\nWrong password, try again")
            else:
                print("\nSomething went wrong, sliha")
                break
