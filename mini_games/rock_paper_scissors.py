import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)
player = None

while player not in choices:
    player = input("rock, paper, or scissors? ").lower()

if player == computer:
    print("Computer:", computer)
    print("Player:", player)
    print("TIE")
elif player == "rock":
    if computer == "paper":
        print("Computer:", computer)
        print("Player:", player)
        print("LOSE")
    if computer == "scissors":
        print("Computer:", computer)
        print("Player:", player)
        print("WIN")
elif player == "paper":
    if computer == "scissors":
        print("Computer:", computer)
        print("Player:", player)
        print("LOSE")
    if computer == "rock":
        print("Computer:", computer)
        print("Player:", player)
        print("WIN")
elif player == "scissors":
    if computer == "rock":
        print("Computer:", computer)
        print("Player:", player)
        print("LOSE")
    if computer == "paper":
        print("Computer:", computer)
        print("Player:", player)
        print("WIN")