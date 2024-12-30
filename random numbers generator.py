#Random numbers game
import random
#Set the min and max value so that computer can pick random number
minimum_number = 1
maximum_number = 10

#Will then print out the amount of attempts the user did
attempts = 1

#Will allow the computer to randomly pick the number
computer_picked_number = random.randint(minimum_number, maximum_number)
#Will print out the random guessed number for debugging
#print(computer_picked_number)

#Will ask the user to input a number between 1-10
user_picked_number = int(input("Enter a number from 1 to 10: "))

#Will print out error if the user went out of range
while user_picked_number<minimum_number or user_picked_number>maximum_number:
    print("Out of range try again!")
    user_picked_number = int(input("Enter a number from 1 to 10:"))

#Will ask the user to enter in number again if it didn't match the random number
while user_picked_number>computer_picked_number or user_picked_number<computer_picked_number:
    print("You didn't guessed the right number!")
    #Will then ask the user to pick the higher number
    if user_picked_number < computer_picked_number:
        print(f"The number is bigger than {user_picked_number}")
        attempts += 1 #Will add an attempt
        # Will then ask the user to pick the lower number
    if user_picked_number > computer_picked_number:
        print(f"The number is lower than {user_picked_number}")
        attempts += 1 #Will add an attempt
        #Will then ask the user to print the number in again
    user_picked_number = int(input("Enter a number from 1 to 10:"))


 #Will exist the game once the user have guessed the right number
print(f"You have guessed the right number within {attempts} attempts!")

