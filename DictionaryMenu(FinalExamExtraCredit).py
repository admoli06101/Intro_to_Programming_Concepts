menu = {
    "burger": 5.99,
    "pizza": 8.99,
    "salad": 4.99,
    "soda": 1.99,
    "fries": 2.99
}

total = 0.0

while True:
    item = input()

    if item == "done":
        break

    if item in menu:
        total = total + menu[item]
    else:
        print("Item not found")

print("Total amount:", total)

print("Aiden Molinary")