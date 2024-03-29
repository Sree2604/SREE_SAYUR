'''Bowling game with one change. The input to the code is, pins knocked for each frame and for all the frames.
 Output is total points. You only have to display the total points , not the points the end of each frame. 
Sample input 10,10,10,10,10,10,10,10,10,10,10,10'''
frames = []
frame = 1

def calculateScore(frames):
    scores = []
    for i in range(len(frames)):
        if frames[i][0] == 10:

            if i <= 7 and frames[i+1][0] == 10 :
                scores.append(frames[i][0] + frames[i+1][0] + frames[i+2][0])

            elif i == 8 and frames[i+1][0] == 10:
                scores.append(frames[i][0] + frames[i+1][0])

            elif i == 9 and frames[i][0] == 10:
                scores.append(frames[i][0])

            else:
                scores.append(frames[i][0] + frames[i+1][0] + frames[i+1][1])

        elif (frames[i][0] + frames[i][1]) == 10:
            scores.append(frames[i+1][0] + frames[i][0] + frames[i][1])

        else:
            scores.append(frames[i][0] + frames[i][1])

    return sum(scores) 

def inputRoll():
    '''In this function the user have to input the number of pins knocked down for two times.
    The input should be in the range of 0 and 10 otherwise it will ask the user to input again.
    If the first input of pins is 10, then it will automatically assign 0 to second input of pins.
    Or else the second input of pins should not exceed the remainingPins value. After getting inputs
    it will append those inputs to list rolls and the return value is rolls'''
    rolls = []      #creating a list named as "rolls"
    pins = int(input("Enter number of pins knocked down in digits: ")) # getting the input from user for knocked down pins

    while pins < 0 or pins > 10:        
        'ask the user to input while the input is less than 0 or greater than 10'
        print("Invalid Input.Enter number of pins between 0 and 10")
        pins = int(input("Enter number of pins knocked down: "))
    rolls.append(pins)      #appending the pins to rolls..
    remainingPins = 10 - pins   #reducing pins from 10
    
    if pins == 10:
        rolls.append(0)     #if the user input is 10 it will automatically append 0 to rolls

    else:
        pins = int(input("Enter number of pins knocked down: "))    #else ask the user to input for second pin
        while pins > remainingPins:
            'if the input pins exceeds the remaingPins, here the user have to enter the input again...'
            print(f"Invalid Input. Your remaining pins are {remainingPins}")
            pins = int(input("Enter number of pins knocked down: "))
        rolls.append(pins)  #again it will append the pins to rolls

    return rolls    #and returns the list rolls

while frame <= 10:
    #getting inputs for 10 frames in this loop...
    print(f'Frame {frame}:')
    rolls = inputRoll()     #calling inputRoll function to get the rolls...
    frames.append(rolls)    #appending the return value of inputRolls to frames...
    frame += 1              #incrementig the frame by one..

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