seats = {}
for i in range(1, 21):
    seats[i] = "available"

first_class = [1, 2, 3, 4, 5]

business_class = [6, 7, 8, 9, 10]

emergency = [11, 12]


def show_seats():
    print("\nSeat Map:")
    for i in range(1, 21):
        print("Seat", i, "-", seats[i])


def buy_seat():
    while True:
        show_seats()

        choice = input("\nEnter a seat number to purchase (or type 'done' to finish): ")

        if choice == "done":
            break

        if not choice.isdigit():
            print("Invalid input.")
            continue

        seat_num = int(choice)

        if seat_num < 1 or seat_num > 20:
            print("Seat does not exist.")
            continue

        if seats[seat_num] == "taken":
            print("Seat already taken.")
            continue

        if seat_num in emergency:
            answer = input("This is an emergency seat. Can you assist in an emergency? (yes/no): ")
            if answer.lower() != "yes":
                print("You must accept responsibility to sit here.")
                continue

        if seat_num in first_class:
            confirm = input("This is a first-class seat. There will be an upcharge. Continue? (yes/no): ")
            if confirm.lower() != "yes":
                print("Seat not purchased.")
                continue

        elif seat_num in business_class:
            print("This is a business-class seat. No extra fee.")

        else:
            print("This is a regular seat.")

        seats[seat_num] = "taken"
        print("Seat", seat_num, "successfully purchased!")


print("Welcome to Better Airlines!")

buy_seat()

print("\nFinal Seating:")
show_seats()

print("\nThank you for your purchase at Better Airlines! Hope to fly with you soon!")