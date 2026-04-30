hours = int(input("Enter the KW hours used: "))

rate1 = 7.633
rate2 = 9.259

if hours <= 1000:
    cost_cents = hours * rate1
else:
    cost_cents = (1000 * rate1) + ((hours - 1000) * rate2)

cost_dollars = cost_cents / 100

print("Amount owed is $" + str(cost_dollars))