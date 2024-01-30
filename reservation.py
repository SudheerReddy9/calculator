# def initialize_seating_chart():
#     return ["A"] * 10

# def display_seating_chart(seating_chart):
#     print("Seating Chart:")
#     for i, seat in enumerate(seating_chart, start=1):
#         print(f"Row {i}: {'Available' if seat == 'A' else 'Occupied'}")

# def first_class(seating_chart):
#     for i in range(5):
#         if seating_chart[i] == "A":
#             seating_chart[i] = "X"
#             return f"Your seat in First Class is Row {i + 1}"
#     return "First Class is full."

# def economy(seating_chart):
#     for i in range(5, 10):
#         if seating_chart[i] == "A":
#             seating_chart[i] = "X"
#             return f"Your seat in Economy is Row {i + 1}"
#     return "Economy is full."

# def menu(seating_chart):
#     while True:
#         print("\nMenu:")
#         print("1. First Class")
#         print("2. Economy")
#         print("3. Exit")
#         choice = input("Please select an option (1/2/3): ")
        
#         if choice == "1":
#             result = first_class(seating_chart)
#             if result == "First Class is full.":
#                 print(result)
#             else:
#                 print(result)
#                 display_seating_chart(seating_chart)
#         elif choice == "2":
#             result = economy(seating_chart)
#             if result == "Economy is full.":
#                 print(result)
#             else:
#                 print(result)
#                 display_seating_chart(seating_chart)
#         elif choice == "3":
#             print("Thank you for using the airline reservation system.")
#             break
#         else:
#             print("Invalid option. Please select a valid option (1/2/3).")

# def main():
#     seating_chart = initialize_seating_chart()
#     menu(seating_chart)

# if __name__ == "__main__":
#     main()
def initialize_seating_chart():
    return ['A'] * 10

def display_seating_chart(seating_chart):
    print("Seating Chart:")
    for i, seat in enumerate(seating_chart ):
        print({'A' if seat == 'A' else 'X'})

def first_class(seating_chart):
    seat_number = int(input("Enter a seat number between 1 and 5: "))

    if 1 <= seat_number <= 5:
        if seating_chart[seat_number - 1] == 'A':
            seating_chart[seat_number - 1] = 'X'
            print(f"Seat {seat_number} in First Class has been reserved.")
        else:
            print(f"Seat {seat_number} is already occupied.")
    else:
        print("Invalid seat number. Please select a seat between 1 and 5.")

def economy(seating_chart):
    seat_number = int(input("Enter a seat number between 6 and 10: "))

    if 6 <= seat_number <= 10:
        if seating_chart[seat_number - 1] == 'A':
            seating_chart[seat_number - 1] = 'X'
            print(f"Seat {seat_number} in Economy Class has been reserved.")
        else:
            print(f"Seat {seat_number} is already occupied.")
    else:
        print("Invalid seat number. Please select a seat between 6 and 10.")

def menu(seating_chart):
    while True:
        print("\nMenu:")
        print("1. First Class")
        print("2. Economy")
        print("3. Exit")

        choice = int(input("Select an option: "))

        if choice == 1:
            first_class(seating_chart)
        elif choice == 2:
            economy(seating_chart)
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

        display_seating_chart(seating_chart)

def main():
    seating_chart = initialize_seating_chart()
    menu(seating_chart)

if __name__ == "__main__":
    main()
