'''
1. Write an app for a cafe. Decide on the items in the cafe, stock of each item in the morning, 
stock in the evening, sales amount at the end of the day and profit for each item. You need to restock an item 
if the supply reaches 20% of the stock. Print the 3 items with highest sales, and top 3 highest profit.(Using Dictionary...)
'''

#defining two lists for quantity
quantityInWords = ['one','two','three','four','five','six','seven','eight','nine']
quantityInDigits = ['1','2','3','4','5','6','7','8','9']

#defining some variables
totalTime = 12
time = 0
addTime = 1
customer = 0
 
itemsInCafe = {
    'coffee' : 
    {
        'name' : 'coffee',
        'price' : 20,
        'stock' : 20,
        'refill' : 20,
        'profit' : 8,
        'totalProfit' : 0,
        'sales' : 0,
        'type' : 'hot'
    },
    'tea' : 
    {
        'name' : 'tea',
        'price' : 25,
        'stock' : 35,
        'refill' : 35,
        'profit' : 10,
        'totalProfit' : 0,
        'sales' : 0,
        'type' : 'hot'
    },
    'milkshake' : 
    {
        'name' : 'milkshake',
        'price' : 45,
        'stock' : 25,
        'refill' : 25,
        'profit' : 18,
        'totalProfit' : 0,
        'sales' : 0,
        'type' : 'cold'
    },
    'coke' : 
    {
        'name' : 'coke',
        'price' : 30,
        'stock' : 30,
        'refill' : 30,
        'profit' : 5,
        'totalProfit' : 0,
        'sales' : 0,
        'type' : 'cold'
    }
}

def topProfitSales():

    '''This function helps to calculate the total profit of each item and print the top three 
    sales and profit...'''

    #calculating the total profit for each item
    for i in itemsInCafe:
        x = itemsInCafe.get(i)
        x['totalProfit'] = x['profit'] * x['sales']
    
    #sort the dictionary by values associated with sales, totalProfit and store it into a list of tuple
    sortedSales = sorted(itemsInCafe.items(), key=lambda x: x[1]['sales'], reverse=True)
    sortedProfit = sorted(itemsInCafe.items(), key=lambda x: x[1]['totalProfit'], reverse=True)

    #printing the top 3 sales and profit....
    print('\nTop 3 Sales...')
    for i,j in sortedSales[:3]:
        print(f"{i} - {j['sales']}")
    print('\nTop 3 Profit...')
    for i,j in sortedProfit[:3]:
        print(f"{i} - {j['totalProfit']}")

def itemRestock(item):
    '''if the stock of item reaches 20%, refill again'''
    if customer % 5 == 0:
        itemsInCafe[item]['stock'] =  itemsInCafe[item]['refill']
        return True

def processCustomerInput(customerInput):
    '''this function is used to process the input to find the items ordered and quantity of it....'''
    cInput = customerInput.split()  #split the customer input into a variable
    print(cInput)
    global quantity,item    #definig two global variables

    for i,j in itemsInCafe.items():
        if i in cInput:
        #processing what are the items ordered and quantity of items...
            item = i
            index = (cInput.index(i)) - 1 
            for k in range(len(quantityInWords)):
                if quantityInWords[k] in cInput[index] or quantityInDigits[k] in cInput[index]:
                    quantity = int(quantityInDigits[k])

            #passing item as arg to check need of restocking   
            repelnish = itemRestock(item)
            print(repelnish)
            j['stock'] -= quantity  #reducing the stock quantity of item
            j['sales'] += quantity  #adding the sales quantity of item
    
def main(time):
    '''greeting the customer and printing the items in cafe...'''
    print("...Warm greetings to our customers...")
    print("")
    print("....MENU....")
    for i in itemsInCafe:
        #print the items in the cafe
        print(i.upper())
    print("")
    global customer
    while time < totalTime:
    #using while loop to check if time is less than total time 
        #getting the input from user in the below format and add time 
        customerInput = input("What do u want...: ")    #input format: two coffee and 6 tea
        time += addTime 
        customer+=1
        processCustomerInput(customerInput.lower())     #passing userinput to a func as a arg...
    for i,j in itemsInCafe.items():
        j['stock'] = j['refill']
    print("Supply replenished at the end of the day...")
    topProfitSales()    #calculating top profit and sales

main(time)  #calling the main function by passing time as arg...            