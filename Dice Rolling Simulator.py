#Dice Rolling Simulator

import random

def main():
    player1 = 0
    player1wins = 0
    player2 = 0
    player2wins = 0
    rounds = 1

    while rounds != 6:
        print("Round " +str(rounds))
        player1 = dice_roll()
        player2 = dice_roll()
        print("Player 1 rolls: " +str(player1))
        print("Player 2 rolls: " +str(player2))
        rounds = rounds + 1

        if player1 == player2:
            print("Draw!\n ")
        elif player1 > player2:
             player1wins = player1wins + 1 #counting player1 rounds
             print("Player 1 wins!\n")
        else:
            player2wins = player2wins + 1 #counting player2 rounds
            print("Player 2 wins!\n")

    if player1wins == player2wins:
        print("Draw!")
    elif player1wins > player2wins:
        print("Player 1 wins! Rounds won: " +str(player1wins) + ".")
    else:
        print("Player 2 wins! Rounds won: " +str(player2wins) + ".")

def dice_roll():
    diceRoll = random.randint(1, 6)
    return diceRoll

main()
