def circle_area(pi, radius):
    return pi * radius * radius


def total_due(money, tax):
    return money + (money * tax)


def to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5/9)


radius = float(input("Enter the radius: "))
pi = 3.14
area = circle_area(pi, radius)
print(area)

money = float(input("Enter the amount of money: "))
tax_input = input("Enter the tax rate: ")

tax = float(tax_input.replace('%', '')) / 100

total = total_due(money, tax)
print(total)

fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
celsius = to_celsius(fahrenheit)
print(celsius)