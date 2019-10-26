from random import randint

choose = ["Rock", "Paper", "Scissors"]
computer = choose[randint(0,2)]
player = False

while player == False:
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock" or "rock":
        if computer == "Paper" or "paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper" or "paper":
        if computer == "Scissors" or "scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors" or "scissors":
        if computer == "Rock" or "rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("Try again. Choose a valid option!")

    player = False
    computer = choose[randint(0,2)]
