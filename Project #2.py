class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        return self.name + " - $" + format(self.price, ".2f")


class VendingMachine:
    def __init__(self):
        self.beverages = {
            "1": Beverage("Dasani", 99.99),
            "2": Beverage("Rootbeer", 19.99),
            "3": Beverage("Voss", 19.99),
            "4": Beverage("Mountain Dew", 19.99),
            "5": Beverage("OSPUZE", 0.69),
            "6": Beverage("Dr Pepper", 1.67)
        }

    def display_menu(self):
        print("\n--- Vending ScaMachine Menu ---")
        for key in self.beverages:
            beverage = self.beverages[key]
            print(key + ". " + beverage.display())

    def select_beverage(self):
        choice = input("Select a beverage (1-6): ")
        if choice in self.beverages:
            return self.beverages[choice]
        else:
            print("Invalid selection. Please try again.")
            return None

    def process_payment(self, beverage):
        total_inserted = 0.0

        while total_inserted < beverage.price:
            try:
                print("Price: $" + format(beverage.price, ".2f"))
                print("Money inserted: $" + format(total_inserted, ".2f"))
                money = float(input("Insert money: $"))

                if money <= 0:
                    print("Please insert a valid amount.")
                else:
                    total_inserted = total_inserted + money

            except ValueError:
                print("Invalid input. Please enter a number.")

        change = total_inserted - beverage.price
        return change

    def vend(self, beverage, change):
        print("\nDispensing " + beverage.name + "...")
        if change > 0:
            print("Returning change: $" + format(change, ".2f"))
        print("Thank you!\n")


def main():
    machine = VendingMachine()

    while True:
        machine.display_menu()
        beverage = machine.select_beverage()

        if beverage is not None:
            change = machine.process_payment(beverage)
            machine.vend(beverage, change)


main()