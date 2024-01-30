# indices and slices
import random
secretNumber = random.randint(1,100)
print(secretNumber)
count = 0
gamesPlayed = 0
response = "Y"
while (response == "Y"):
    count = 0
    while(count < 10):
        guess = int(input("Guess the secret number: "))
        if guess == secretNumber:
            print("You guessed the secret number")
            if(count == 0):
                print('It took ', count+1, "try to guess the secret number.")
            else:
                print('It took ', count+1, "tries to guess the secret number.")
            break
        elif guess > secretNumber:
            print("Your guess is too high")
        else:
            print("your guess is too ow")
        count =+ 1
    print("The secret number is :", secretNumber)
    gamesPlayed = gamesPlayed + 1
    response = input("Would you like to play another name: Y = Yes, N = No")
print("The number of games played is:", gamesPlayed)