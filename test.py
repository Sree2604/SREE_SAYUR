frame = 1
numberOfPins = 10
score = 0
totalScore = 0
currentFrame = 0

def bonusPoints(firstRoll,secondRoll):
    points = 0
    if firstRoll == 10:
        print("It's a strike...")
    elif (firstRoll+secondRoll == 10):
        return points

# def calculateScore(firstRoll,secondRoll):
    
#     # if frame == 10:
#     #     bonus = bonusPoints(firstRoll,secondRoll)
#     #     return firstRoll + secondRoll + bonus
#     # return firstRoll + secondRoll

def rolls():
    secondRoll = 0
    firstRoll = int(input("Enter first roll the number pins knocked down(in digits): "))
    remainingPins = numberOfPins - firstRoll
    if firstRoll == 10:
        return firstRoll,secondRoll
    else:
        secondRoll =  int(input("Enter second roll the number pins knocked down(in digits): "))
        if secondRoll > remainingPins:
            print(f"Invalid input. Second Roll limit should less than or equal to {remainingPins}")
            secondRoll = int(input("Enter second roll the number pins knocked down(in digits):"))
        return firstRoll,secondRoll


while frame != 11:
    print(f"Frame:{frame}")
    rollValues = rolls()
    score = calculateScore(rollValues[0],rollValues[1])
    totalScore += score
    print(f"Score of frame {frame} is {score}")
    print(totalScore)
    frame+=1
print(f"Maximum Score: {totalScore}")

while True:
    rollValues = rolls()
    