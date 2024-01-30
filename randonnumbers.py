import random

def random_numbers(num):
 # To count the total number in List
 count = 0

 # To count the total number of even numbers in List
 even_numbers = 0

 # To count the total number of odd numbers in List
 odd_numbers = 0

 # To add all the generated random numbers
 sum = 0

 # To count total number of zeros in the List
 zero = 0

 # To check the average of random numbers
 average_of_numbers = 0
 pick_numbers = [random.randint(0, 100) for num in range(num)]
 print("Generated random numbers:")
 for num in pick_numbers:
        
        count = count +1

        sum =  sum + num

        print(num, end=" ")

        #print()

        # To print the output 5 numbers per row
        if count % 5 == 0:

            print()

        # To check the number of zeros in output
        if num == 0:

            zero = zero + 1

        # To check the total number of even numbers in output
        if num % 2 == 0:

            even_numbers = even_numbers + 1


        else :

            # To check the total odd_numbers numbers in the output
            odd_numbers = count - even_numbers

 # To check the average of numbers
 average_of_numbers = sum / count
 print()
# To Display the output 
 if zero == 0:
        print(f"There are {even_numbers} evens which includes no zeros")
 elif zero == 1:
        print(f"There are {even_numbers} evens which includes {zero} zero")
 else:
        print(f'There are {even_numbers} evens which includes {zero} zeros')

 print("Total number of odds", odd_numbers)
 print(f"Sum of numbers {sum:,.2f}")
 print("Average", round(average_of_numbers,2))



# Total number of random numbers need to generate
num = int(input("How many random numbers would you like to generate? "))

# If the integer provided in negative then it prompts the error message
while num<0 or num ==0 or num > 0:
     if num<0:
        print("Error, only positive integer please")
        num = int(input("How many random numbers would you like to generate? "))
        continue
     elif num == 0:
        print("Please enter the number Greater than zero")
        num = int(input("How many random numbers would you like to generate? "))
        continue
     else :
        random_numbers(num)
        break







