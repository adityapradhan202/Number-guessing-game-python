# Number guessing game
import random
attempts = 0
game_level = input("Enter 'easy' for easy level, otherwise enter 'hard': ")

if game_level.lower() == "easy":
    attempts = 10
elif game_level.lower() == "hard":
    attempts = 5
else:
    print("Invalid input!")


random_number = random.randint(1, 100)
flag = True
while flag:
    user_guess = int(input("Guess the number: "))
    if user_guess == random_number:
        print(f"You got it!\nThe number is {random_number}.")
        flag = False
        
    elif user_guess > random_number:
        print("Too high!")
        attempts -= 1
        print(f"You have {attempts} attempts left.")
    elif user_guess < random_number:
        print("Too low!")
        attempts -= 1
        print(f"You have {attempts} attempts left.")
        
    if attempts == 0:
        print(f"You lost!\nThe number was {random_number}.")
        flag = False
        

