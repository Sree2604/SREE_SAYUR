
# ########## Problem 3 ############
# #Write a program for a bag shop. Shop has 100 red bags (each Rs 1000) and 200 white bags (each Rs 1500)
# #Customers can buy one or more bags at a time.
# #The program ends when the sales reached Rs10000 or at least 10 bags are sold. 
# #Display total sales and total number of bags sold

# #initialize variables
redBags, greenBags = 100, 200
totalSales , totalBagsSold = 0,0

while (totalSales < 10000 and totalBagsSold < 10) :
    bagColor = input("Which bag color you need...").lower()     #get the color of bag as input
    bagCount = int(input("How many bags do u need (in digits)..."))     #get also the no of bag as input
    
    #calculate total cost for the bags
    if bagColor == 'red':
        totalSales += bagCount * redBags    #if 'red' calculate respective sales for it
    elif bagColor == 'green':
        totalSales += bagCount * greenBags  #if 'green' calculate respective sales for it
    else:
        print("We have only red nad green colored bag...")  #otherwise ask the user to input again
        bagCount = 0
        continue
    
    totalBagsSold +=  bagCount  #increment no of bags sold  

print (f"Total Sales: {totalSales} and Total Number of bags sold: {totalBagsSold}")   


"""
How many bags do u need (in digits)...2
Which bag color you need...greeb
How many bags do u need (in digits)...2 
We have only red nad green colored bag...
Which bag color you need...green
How many bags do u need (in digits)...2
Which bag color you need...red
How many bags do u need (in digits)...5
Which bag color you need...yellow
How many bags do u need (in digits)...1
We have only red nad green colored bag...
Which bag color you need...green
How many bags do u need (in digits)...10
Total Sales: 3100 and Total Number of bags sold: 19
"""