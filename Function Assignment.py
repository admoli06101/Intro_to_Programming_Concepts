def circle_area(pi, radius):
    return pi * radius * radius

def total_due(money, tax):
    return money + (money * tax)

def to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5/9)


radius = float(input("Enter the radius: "))
pi = 3.14

print(round(circle_area(pi, radius), 2))

money = float(input("Enter the amount of money: "))

tax_input = input("Enter the tax rate (like 6%): ")

tax = float(tax_input.replace('%', '')) / 100

print(round(total_due(money, tax), 2))

fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

print(round(to_celsius(fahrenheit), 5))