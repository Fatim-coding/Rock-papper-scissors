import random

options = ["Rock", "Paper","scissors"]

user_choice = input("choose Rock,paper, or scissors:")

computer_choice = random.choice(options)

print("you chose:", user_choice)
print("computer chose:",computer_choice)

if user_choice == computer_choice:
    print("It's  a title")
elif user_choice == "Rock" and computer_choice == "scissors":
    print("Rock smashes scissors!you win!")
elif user_choice == "paper" and computer_choice == "Rock":
    print("paper covers rock!you win!")
elif user_choice == "Scissors" and computer_choice == "paper":
    print("Scissors cuts paper!you win!")
else:
    print("You lose!")
