frame = 1
numberOfPins = 10
score = 0
totalScore = 0
currentFrame = 0

def bonusPoints(firstRoll,secondRoll):
    points = 0
    if firstRoll == 10:
        print("It's a strike...")
        bonusRoll1 = int(input("Enter the number of pins knocked down on first bonus roll: "))
        bonusRoll2 = int(input("Enter the number of pins knocked down on second bonus roll: "))
        points = bonusRoll1 + bonusRoll2
    elif (firstRoll+secondRoll == 10):
        print("It's a spare...")
        bonusRoll1 = int(input("Enter the number of pins knocked down on first bonus roll: "))
        points = bonusRoll1
    return points

def calculateScore(firstRoll,secondRoll):
    bonus = bonusPoints(firstRoll,secondRoll)
    return firstRoll + secondRoll + bonus
    #return firstRoll + secondRoll

def frames(firstRoll):
    if firstRoll == 10:
        return True
    else:
        return True

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
    checkFrames = frames(rollValues[0])
    if checkFrames == True:
        frame+=1
    currentFrame = frame - 1
    score = calculateScore(rollValues[0],rollValues[1])
    totalScore += score
    print(f"Score of frame {frame - 1} is {score}")
    print(totalScore)

print(f"Maximum Score: {totalScore}")