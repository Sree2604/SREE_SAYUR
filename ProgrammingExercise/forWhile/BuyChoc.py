# #buy choc and cake
# # one choc is Rs 200
# # one cake is 150
# #get budget from user.

noOfCake,noOfChoc = 0,0     #declare required variables

def findQuantity(budget,price):
    quantity = 0    
    while budget >= price:
        #loop until the budget not less than the min price
        quantity += 1       #increase the quantity and reduce the price from budget
        budget -= price     

    return quantity     #return the quantity

budget = int(input("Enter the budget of the user: "))       #get the budget as ipnut

if budget >= 150:   
    #if the budget is 150 or more then call findQuantity func to find quantity of cake
    noOfCake = findQuantity(budget,150)
    print(f"You can buy {noOfCake} cakes from your budget...")
    if budget >= 200:
        #and also if budget is 200 or more the find quantity of choc same as above
        noOfChoc = findQuantity(budget,200)
        print(f"You can buy {noOfChoc} chocs from your budget...")
    
else:
    #otherwise 
    print("You cannot buy anything from the shop...")    

"""
Output:
Enter the budget of the user: 150
You can buy 1 cakes from your budget...

Enter the budget of the user: 800
You can buy 5 cakes from your budget...
You can buy 4 chocs from your budget...

Enter the budget of the user: 140
You cannot buy anything from the shop...
"""


