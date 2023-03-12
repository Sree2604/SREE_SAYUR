'''
1. Write an app for a cafe. Decide on the items in the cafe, stock of each item in the morning, 
stock in the evening, sales amount at the end of the day and profit for each item. You need to restock an item 
if the supply reaches 20% of the stock. Print the 3 items with highest sales, and top 3 highest profit.
'''

itemsInCafe = ['coffee','tea','cappucino','cookie']

itemStock = [50,60,45,35]
itemStockRefill = [50,60,45,35]
itemPrice = [35,45,80,35]

quantityInWords = ['one','two','three','four','five','six','seven','eight','nine']
quantityInDigits = ['1','2','3','4','5','6','7','8','9']


itemSales = [0,0,0,0]
itemProfit = [15,20,25,5]
totalProfit = []
totalSales = []
totalTime = 12
addTime = 4
time = 0

def processCustomerInput(customerInput):
    list1 = list(customerInput.split())
    global quantities 
    quantities = []
    for i in range(len(itemsInCafe)):
        if itemsInCafe[i] in list1:
            index = (list1.index(itemsInCafe[i])) - 1
            for x in range(len(quantityInWords)):
                if quantityInWords[x] in list1[index] or quantityInDigits[x] in list1[index]:
                    quantities.insert(i,int(quantityInDigits[x]))
        else:
            quantities.insert(i,0)   

def addSales():
    for j in range(len(itemsInCafe)):
        if itemStock[j] <= (itemStockRefill[j] * 0.2):
            itemStock[j] = itemStockRefill[j]
            
        itemStock[j] -= quantities[j]
        itemSales[j] += quantities[j]

def calculateProfit():
    for k in range(len(itemsInCafe)):
        itemProfit[k] *= itemSales[k]
        totalProfit.append(f"Rs.{itemProfit[k]} total profit gained from {itemsInCafe[k]}")
        totalSales.append(f"{itemSales[k]} number of {itemsInCafe[k]} have sold")

def topProfitSales():
    i,j = 0,0
    while i!=2 or j!=2:
        if i!=3:
            if i==0:
                print("Top three highest profits....")
            profitIndex = itemProfit.index(max(itemProfit))
            print(f"{max(itemProfit)} profit earned from {itemsInCafe[profitIndex]}")
            itemProfit[profitIndex] = 0
            i+=1
        elif j!=3:
            if j==0:
                print("Top three highest sales....")
            index = itemSales.index(max(itemSales))
            print(f"{max(itemSales)} number of sales on {itemsInCafe[index]}")
            itemSales[index] = 0
            j+=1

def main(time):
    while time < totalTime:
        time += addTime
        customerInput = input("What do u want...: ")
        processCustomerInput(customerInput.lower())
        addSales()
    calculateProfit()
    topProfitSales()


if time == 0:
    print("...Warm greetings to our customers...")
    print("")
    print("(: Here are the items that we can serve you :)")
    for item in range(len(itemsInCafe)):
        print(f"{item+1}. {itemsInCafe[item].upper()}")
    print("")
    main(time)