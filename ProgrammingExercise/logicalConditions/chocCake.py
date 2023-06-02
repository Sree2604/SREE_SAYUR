########## Problem 3 ##########
##buy choc and cake
# one choc is Rs 200
# one cake is 150
#get budget from user. Also get the total number of choc and cakes that the shop has
#Hint - you can buy choc/Cake only if shop has it.

#find how many choc and cake the user can buy.
def orderQuantity(budget,itemStock,price):
    quantity,cost = 0,0     #initializing two variables
    while quantity < itemStock:     #check quantity is less than itemstock
        cost += price       #if true add the price to cost
        if cost > budget:   
            cost -= price   #if the cost greater than budget reduce price from the cost
            break   #and break the loop
        quantity += 1   #increase the quantity count
    return quantity, cost   

cakePrice, chocPrice = 150, 200     #initializing price to cake and choc and print it     
print(f"Cost of One CHOC is Rs {chocPrice}...")
print(f"Cost of One CAKE is Rs {cakePrice}...")

userBudget = int(input("Enter your budget: "))      #get the budget from the user

#enter the number of cakes and chocs that the shop has
cakeStock = int(input("How many cakes the shop has: "))     
chocStock = int(input("How many chocs the shop has: "))

if cakeStock == 0 and chocStock == 0:
    #if there is no stock on the shop...
    print("Sorry currently the shop can't serve you...")
else:
    #stores the quantity of cake and choc in a variable return by the orderQuantity func
    cakesOrder = orderQuantity(userBudget, cakeStock, cakePrice)
    chocsOrder = orderQuantity(userBudget, chocStock, chocPrice)

    #print the number of cakes and chocs the user can buy and also the cost of it...
    print(f"You can buy {cakesOrder[0]} no. of cakes from ur budget and it will cost Rs.{cakesOrder[1]}...")
    print(f"You can buy {chocsOrder[0]} no. of chocs from ur budget and it will cost Rs.{chocsOrder[1]}...")


"""
Output:
Cost of One CHOC is Rs 200...
Cost of One CAKE is Rs 150...
Enter your budget: 800 
How many cakes the shop has: 2
How many chocs the shop has: 6
You can buy 2 no. of cakes from ur budget and it will cost Rs.300...
You can buy 4 no. of chocs from ur budget and it will cost Rs.800...
"""