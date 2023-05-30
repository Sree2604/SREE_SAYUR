# ######## Problem 1 ###############
# #Write a program that prints out a diamond shape using $.
# #After printing each line, wait for user input. If the user presses space, continue
# #If the users presses any other key, stop printing. Maximum 10 lines
def topTriangle(n):
    print(" "*(5-n-1) + "$ "*(n+1))

def bottomTriangle(m):
    print(" "*(m+1) + "$ "*(5-m-1)) 

count,n = 0,0
m = 0
userInput = input("Press space to continue...")
while count < 10 and userInput == ' ':
    if n < 5:
        topTriangle(n)
        n += 1
    else: 
        bottomTriangle(m)
        m+=1       
    
    userInput = input()
    count+=1


# ######## Problem 2 ###############
# # Computer will guess a random number. 
# # user has to guess that number. for each guess, print 'High' or 'Low'
# # eg - computer number - 189
# # user guess 56 - print low
# # user guess 678 - print high
# # Get user input and print 'high' or 'low' until the user guesses the number correctly 
# # https://www.w3schools.com/python/ref_random_randint.asp - read this to learn how to create a random number

import random
computerNo = random.randint(3,9)

attempt = 0
while(True):
    userNo = int(input("Enter you guess...."))
    attempt +=1
    if userNo > computerNo:
        print("You're HIGH...")
    elif userNo < computerNo:
        print("You're LOW...")
    else:
        break

print ("User guessed the number in ", attempt, "attempts")

# ########## Problem 3 ############
# #Write a program for a bag shop. Shop has 100 red bags (each Rs 1000) and 200 white bags (each Rs 1500)
# #Customers can buy one or more bags at a time.
# #The program ends when the sales reached Rs10000 or at least 10 bags are sold. 
# #Display total sales and total number of bags sold

# #initialize variables
redBags, greenBags = 100, 200
totalSales , totalBagsSold = 0,0

while (totalSales < 10000 and totalBagsSold < 10) :
    bagColor = input("Which bag color you need...").lower()
    bagCount = int(input("How many bags do u need (in digits)..."))
    
    #calculate total cost for the bags
    if bagColor == 'red':
        totalSales += bagCount * redBags
    elif bagColor == 'green':
        totalSales += bagCount * greenBags
    else:
        print("We have only red nad green colored bag...")
        bagCount = 0
        continue
    
    totalBagsSold +=  bagCount  #increment no of bags sold

print (f"Total Sales: {totalSales} and Total Number of bags sold: {totalBagsSold}")   