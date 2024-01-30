# Below the function for airline reservation booking.
aligned_seats = []
first_class_filled = ''
economy_class_filled = ''
seating_arrangement = ['A'] * 10
first_class_seats = [number for number in range(1, 6)]
economy_class_seats = [number for number in range(6, 11)]

# initializing the menu of the seating arrangement
def line(first_class_filled, economy_class_filled):
    sections = ["1. First Class", "2. Economy Class", "3. Exit"]
    seats = ["(Rows: 1 to 5)" , "(Rows: 6 to 10)", ""]
    if seating_arrangement[:5] == ['X'] * 5:
        first_class_filled = 'Full'
    if seating_arrangement[5:] == ['X'] * 5:
        economy_class_filled = 'Full' 
    avaliability = [first_class_filled, economy_class_filled, '']
    
    for seats, sections, avaliability in zip(seats, sections, avaliability):
        
        print(f'{sections:<30} {seats:<15} {avaliability:>20}')


# selecting the seat in first class
def first_class():   
    seat_number = int(input("Please select your seat number (1 - 5) :"))
    if 1 <= seat_number <= 5:
        if seating_arrangement[seat_number - 1] == 'A':
            seating_arrangement[seat_number - 1] = 'X'
            print(f"seatnumber {seat_number} is reserved")
            print(seating_arrangement,"")
        else :
            print("This seat is not avaliable. Please select another seat.")
        
    else:
        print("This seat is not in the First Class section.")
        first_class()
        

# selecting the seat in economy class
def economy_class():
    seat_number = int(input("Please select your seat number (6 - 10) :"))
    if 6 <= seat_number <= 10:
        if seating_arrangement[seat_number - 1] == 'A':
            seating_arrangement[seat_number - 1] = 'X'
            print(f"seatnumber {seat_number} is reserved.")
            print(seating_arrangement,"")
        
        else :
            print("This seat is not avaliable. Please select another seat.")

    else:
        print("This seat is not in the Economy class section.")
        economy_class()


# Declaring the menu based on user input
def menu():
    while True:
        line(first_class_filled, economy_class_filled)
        print("Seating chart: " ,seating_arrangement)
        choice = int(input("choice ==>"))


 # Code for full seat booking declaration
        if choice == 1 :
            if (seating_arrangement[:5] != ['X'] * 5):
                first_class()
            else:
                print('First Class is full. Choose Economy class instead !!!')
        elif choice == 2 :
            if (seating_arrangement[5:] != ['X'] * 5):
                economy_class()
            else:
                print('Economy Class is full.')
        elif choice == 3:
            break
        else:
            print("Invalid input. Please option 1, 2 or 3")
menu()
