def print_menu():
    print("\nTaco Palace Menu")
    print("1. Taco")
    print("2. Burrito")
    print("3. Nachos")
    print("4. Soft Drink")
    print("5. Quit")

def get_price(choice):
    if choice == 1:
        return 2.50
    elif choice == 2:
        return 5.00
    elif choice == 3:
        return 4.00
    elif choice == 4:
        return 1.75
    else:
        return 0

def get_name(choice):
    if choice == 1:
        return "Taco"
    elif choice == 2:
        return "Burrito"
    elif choice == 3:
        return "Nachos"
    elif choice == 4:
        return "Drink"


print("Welcome to Taco Palace, please view the menu below and enter the number that represents your selection.")

order = []
total = 0

while True:
    print_menu()
    choice = int(input("User entered: "))

    if choice == 5:
        break
    elif choice >= 1 and choice <= 4:
        item = get_name(choice)
        print("You selected a " + item)
        order.append(item)
        total = total + get_price(choice)
    else:
        print("Invalid selection")

if len(order) == 0:
    print("You ordered nothing. Your total is $0")
elif len(order) == 1:
    print("You ordered a " + order[0] + ". Your total is $" + str(total))
else:
    output = "You ordered "
    for i in range(len(order)):
        if i == len(order) - 1:
            output = output + "and a " + order[i]
        else:
            output = output + "a " + order[i] + ", "
    print(output + ". Your total is $" + str(total))




print("Aiden Molinary")
