import random 

state = ''

row =  random.randrange(1,7)
col = random.randrange(1,7)
spot = (row,col)

player1Score = 0
player2Score = 0

player1Spots = []
player2Spots = []

def checkValid(spot):
    # if spot in player1Spots:
    #     return False,"The spot is claimed by the player 1"
    # elif spot in player2Spots:
    #     return False,"The spot is claimed by the player 2"
    # else:
    #     return True
    if spot not in player1Spots and spot not in player2Spots:
        return True
    else:
        return False

# def calculateScore(spot,player):
#     if player == 1:
#         if spot in player2Spots:
#             player1Score+=1
#         else:
#             for i,j in rang

def rollDice(player):
    start = confirmStart()
    if start == True:
        row =  random.randrange(1,7)
        col = random.randrange(1,7)
        spot = (row,col)
        if player == 1 :
            valid = checkValid(spot)
            if valid == True:
                player1Spots.append(spot)
            #calculateScore(spot,1)
        else:
            valid = checkValid(spot)
            if valid == True:
                player2Spots.append(spot)
            #calculateScore(spot,2)                

def confirmStart():
    state = input('Press "s" to roll the dice...')
    if state.lower() == 's':
        return True
    else:
        return False
while (player1Score != 5 and player2Score != 5):
    # start = confirmStart()
    # if start == True:
    rollDice(1)
    rollDice(2)
