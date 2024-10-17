import random

choice_list = ["paper", "rock", "scissors"]

player_choice = input("Write paper, rock or scissors to play\n").lower()
print("You chose " + player_choice)
computer_choice = choice_list[random.randint(0, 2)]
print("Computer chose " + computer_choice)

if player_choice == computer_choice:
    print("Its a draw.")
elif (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "rock" and computer_choice == "scissors"):
    print("You win!")
elif (player_choice == "rock" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "rock"):    
    print("Computer wins!")
else:
    print("Type a valid option")