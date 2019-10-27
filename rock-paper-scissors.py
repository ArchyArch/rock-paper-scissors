from random import randint
from sys import exit

choose = ["Rock", "Paper", "Scissors"]
computer = choose[randint(0,2)]
player = False
answer = "maybe"

while player == False:
    while answer != "yes" or answer != "no":
        player = input("Rock, Paper, Scissors?")
        if player.lower() == computer.lower():
            print("Tie!")
        elif player.lower() == "rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
            else:
                print("You win!", player, "smashes", computer)
        elif player.lower() == "paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
            else:
                print("You win!", player, "covers", computer)
        elif player.lower() == "scissors":
            if computer == "Rock":
                print("You lose...", computer, "smashes", player)
            else:
                print("You win!", player, "cut", computer)
        else:
            print("Try again. Choose a valid option!")

        answer = input("Do you want to play again? Yes or no ")

        if answer.lower() == "yes":
            player = False
            computer = choose[randint(0,2)]
        elif answer.lower() == "no":
            exit()
        else:
            answer = input("Try again. Choose a valid option! ")
