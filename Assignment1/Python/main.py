"""System module."""
import random
choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
PLAYER = False
CPU_SCORE = 0
PLAYER_SCORE = 0
while True:
    PLAYER = input("Rock, Paper or  Scissors?").capitalize()
    # Conditions of Rock,Paper and Scissors
    if PLAYER == computer:
        print("Tie!")
    elif PLAYER == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", PLAYER)
            CPU_SCORE = CPU_SCORE+1
        else:
            print("You win!", PLAYER, "smashes", computer)
            PLAYER_SCORE = PLAYER_SCORE+1
    elif PLAYER == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", PLAYER)
            CPU_SCORE = CPU_SCORE+1
        else:
            print("You win!", PLAYER, "covers", computer)
            PLAYER_SCORE = PLAYER_SCORE+1
    elif PLAYER == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", PLAYER)
            CPU_SCORE = CPU_SCORE+1
        else:
            print("You win!", PLAYER, "cut", computer)
            PLAYER_SCORE = PLAYER_SCORE+1
    elif PLAYER == 'End':
        print("Final Scores:")
        print(f"CPU:{CPU_SCORE}")
        print(f"Plaer:{PLAYER_SCORE}")
        break
