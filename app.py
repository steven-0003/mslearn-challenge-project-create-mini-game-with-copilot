#Create a rock paper scissors game using Github Copilot

import random

#Create a list of options with the following: rock, paper, scissors
options = ["rock", "paper", "scissors"]

#Create a variable called score and rounds_played and set them to 0
score = 0
rounds_played = 0

#Create a while loop that runs until the user decides to quit
while True:
    #Ask the user to input their choice (rock, paper, or scissors)
    user_choice = input("Enter your choice (rock, paper, or scissors): ")

    #Convert the user_choice to lowercase
    user_choice = user_choice.lower()

    #Check if the user's choice is valid
    if user_choice not in options:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        continue

    #Generate a random choice for the computer
    computer_choice = random.choice(options)

    #Print the choices of the user and the computer
    print(f"User choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")

    #Check the outcome of the game and update the score and rounds_played accordingly
    rounds_played += 1

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
        score += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
        score += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        score += 1
    else:
        print("You lose!")
 
    #Ask the user if they want to play again
    play_again = input("Do you want to play again? (y/n): ")
    #If the user chooses to quit, print the final score and rounds_played and exit the loop
    if play_again.lower() != "y":
        print(f"Final score: {score}")
        print(f"Rounds played: {rounds_played}")
        break

    