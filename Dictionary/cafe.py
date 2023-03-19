'''
1. Write an app for a cafe. Decide on the items in the cafe, stock of each item in the morning, 
stock in the evening, sales amount at the end of the day and profit for each item. You need to restock an item 
if the supply reaches 20% of the stock. Print the 3 items with highest sales, and top 3 highest profit.
'''
quantityInWords = ['one','two','three','four','five','six','seven','eight','nine']
quantityInDigits = ['1','2','3','4','5','6','7','8','9']

totalTime = 12
addTime = 4

items = {
    'coffee' : 
    {
        'name' : 'coffee',
        'price' : 20,
        'stock' : 20,
        'refill' : 20,
        'profit' : 8,
        'sales' : 0
    },
    'tea' : 
    {
        'name' : 'tea',
        'price' : 25,
        'stock' : 35,
        'refill' : 35,
        'profit' : 10,
        'sales' : 0
    },
    'sandwich' : 
    {
        'name' : 'sandwich',
        'price' : 45,
        'stock' : 25,
        'refill' : 25,
        'profit' : 18,
        'sales' : 0
    },
    'fries' : 
    {
        'name' : 'fries',
        'price' : 30,
        'stock' : 30,
        'refill' : 30,
        'profit' : 5,
        'sales' : 0
    }
}

def processCustomerInput(customerInput):
    list1 = list(customerInput.split())
    global quantity
    #quantities = []
    for i in items:
        x = items.get(i)
        if i in list1:
            index = (list1.index(i)) - 1 
            for k in range(len(quantityInWords)):
                if quantityInWords[k] in list1[index] or quantityInDigits[k] in list1[index]:
                    quantity = int(quantityInDigits[k])
            x['stock'] -= quantity
            x['sales'] += quantity

customerInput = input("What do u want...: ")
processCustomerInput(customerInput.lower())
print(items['coffee'])
'''
def main(time):
    while time < totalTime:
        time += addTime
        customerInput = input("What do u want...: ")
        processCustomerInput(customerInput.lower())
main()
'''