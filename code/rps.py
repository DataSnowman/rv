# write a rock paper scissors program in python

import random 
  
print("Let's play Rock Paper Scissors!")  
  
# Define the valid options  
options = ["rock", "paper", "scissors"]  
  
# Get the user's choice  
user_choice = input("Enter your choice (rock/paper/scissors): ").lower()  
  
# Validate the user's choice  
while user_choice not in options:  
    user_choice = input("Invalid choice. Enter your choice (rock/paper/scissors): ").lower()  
  
# Generate the computer's choice  
computer_choice = random.choice(options)  
  
# Display the choices  
print(f"\nYou chose {user_choice}.")  
print(f"The computer chose {computer_choice}.\n")  
  
# Determine the winner  
if user_choice == computer_choice:  
    print("It's a tie!")  
elif user_choice == "rock":  
    if computer_choice == "paper":  
        print("Computer wins!")  
    else:  
        print("You win!")  
elif user_choice == "paper":  
    if computer_choice == "scissors":  
        print("Computer wins!")  
    else:  
        print("You win!")  
elif user_choice == "scissors":  
    if computer_choice == "rock":  
        print("Computer wins!")  
    else:  
        print("You win!") 

