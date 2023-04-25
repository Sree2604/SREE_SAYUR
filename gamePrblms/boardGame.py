""" 1. Write an app for the follwoing two player game. You have a 6 x 6 board. 
Users take turns rolling the dice twice. first roll is row no, second roll is col number. Mark the spot (row, col) as claimed by the user
who rolled the dice.
When the user rolls the dice within 1 col/row of a claimed spot of the other user, the other user gets a point. 
If the spot is same as the claimed spot of the other user, the user that rolled the dice gets a point. 
The player who gets 5 points first wins the game. """

import random 

state = ''
player1Score = 0
player2Score = 0

player1Spots = []
player2Spots = []

def checkValid(spot):
    if spot not in player1Spots and spot not in player2Spots:
        return True
    else:
        return False

def calculateScore(spot,player):
    global player1Score,player2Score
    if player == 1:
        if spot in player2Spots:
            player1Score+=1
        elif spot in player1Spots:
            player1Score+=0
        else:
            for i in player2Spots:
                diff = tuple(map(lambda i, j: i - j, i, spot))
                print(diff)
                if diff[0] == 1 or diff[1] == 1:
                    player2Score+=1
                    break
    else:
        if spot in player1Spots:
            player2Score+=1
        elif spot in player2Spots:
            player2Score+=0
        else:
            for i in player1Spots:
                diff = tuple(map(lambda i, j: i - j, i, spot))
                print(diff)
                if diff[0] == 1 or diff[1] == 1:
                    player1Score+=1
                    break

def confirmStart():
    state = input('Press "s" to roll the dice...')
    if state.lower() == 's':
        return True
    else:
        return False

def rollDice(player):
    start = confirmStart()
    if start == True:
        row =  random.randrange(1,7)
        col = random.randrange(1,7)
        spot = (row,col)
        print(spot)
        #sprint(type(spot))
        if player == 1 :
            valid = checkValid(spot)
            if valid == True:
                player1Spots.append(spot)
            calculateScore(spot,1)
        else:
            valid = checkValid(spot)
            if valid == True:
                player2Spots.append(spot)
            calculateScore(spot,2)                


while (player1Score != 5 and player2Score != 5):
    print("")
    print("Player 1 Turn")
    rollDice(1)
    print("Player 2 Turn")
    rollDice(2)
    print(f"Player-1 score:{player1Score}")
    print(f"Player-2 score:{player2Score}")

print("")
if player1Score == 5:
    print("Player 1 wins...")
else:
    print("Player 2 wins...")