frames = []
frame = 1

def calculateScore(frames):
    new = []
    new.extend(enumerate(frames))
    scores = []
    for i in range(len(new)):
        if new[i][1][0] == 10:
            if i <= 7 and new[i+1][1][0] == 10 :
                scores.append(new[i][1][0] + new[i+1][1][0] + new[i+2][1][0])
            elif i == 8 and new[i+1][1][0] == 10:
                scores.append(new[i][1][0] + new[i+1][1][0])
            elif i == 9 and new[i][1][0] == 10:
                scores.append(new[i][1][0])
            else:
                scores.append(new[i][1][0] + new[i+1][1][0] + new[i+1][1][1])
        elif (new[i][1][0] + new[i][1][1]) == 10:
            scores.append(new[i+1][1][0] + new[i][1][0] + new[i][1][1])
        else:
            scores.append(new[i][1][0] + new[i][1][1])

    return sum(scores) 

def inputRoll():
    rolls = []
    pins = int(input("Enter number of pins knocked down: "))
    while pins < 0 or pins > 10:
        print("Invalid Input.Enter number of pins between 0 and 10")
        pins = int(input("Enter number of pins knocked down: "))
    rolls.append(pins)
    remainingPins = 10 - pins
    if pins == 10:
        rolls.append(0)
    else:
        pins = int(input("Enter number of pins knocked down: "))
        while pins > remainingPins:
            print(f"Invalid Input. Your remaining pins are {remainingPins}")
            pins = int(input("Enter number of pins knocked down: "))
        rolls.append(pins)
    return rolls

while frame <= 10:
    print(f'Frame {frame}:')
    roll = inputRoll()
    frames.append(roll)
    frame += 1
scores = calculateScore(frames)
print(f'Total Score is {scores}')
""" frame = 1
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
    if frame == 10:
        bonus = bonusPoints(firstRoll,secondRoll)
        return firstRoll + secondRoll + bonus
    return firstRoll + secondRoll

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

print(f"Maximum Score: {totalScore}") """