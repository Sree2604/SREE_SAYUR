
# ######## Problem 2 ###############
# # Computer will guess a random number. 
# # user has to guess that number. for each guess, print 'High' or 'Low'
# # eg - computer number - 189
# # user guess 56 - print low
# # user guess 678 - print high
# # Get user input and print 'high' or 'low' until the user guesses the number correctly 
# # https://www.w3schools.com/python/ref_random_randint.asp - read this to learn how to create a random number

import random       #import the random module from pyhton lib
computerNo = random.randint(3,9)           #generate num randomly between 3,9

attempt = 0     
while(True):
    #loop until the user guess correctly
    userNo = int(input("Enter you guess...."))      #ask the user to enter their guessed num
    attempt +=1     #increase the no of attempt
    if userNo > computerNo: 
        #if the input is greater than correct num then print "High"
        print("You're HIGH...")
    elif userNo < computerNo:
        #if the input is lower than correct num then print "low"
        print("You're LOW...")
    else:
        #if the user finds the num then break the loop
        break

print ("User guessed the number in ", attempt, "attempts")      #print the no of attempts

"""
Output:
Enter you guess....1 
You're LOW...
Enter you guess....5
You're LOW...
Enter you guess....6
You're LOW...
Enter you guess....9
You're HIGH...
Enter you guess....7
You're LOW...
Enter you guess....8
User guessed the number in  6 attempts
"""