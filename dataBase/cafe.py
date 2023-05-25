import mysql.connector

quantityInWords = ['one','two','three','four','five','six','seven','eight','nine']
quantityInDigits = ['1','2','3','4','5','6','7','8','9']

totalTime = 12
addTime = 4
time = 0

cafeDB = mysql.connector.connect(
    host='localhost',
    username='root',
    password='Sreearangs@2604',
    database = 'cafe'
)

mycursor = cafeDB.cursor()


def processCustomerInput(customerInput,details):
    '''this function is used to process the input to find the items ordered and quantity of it....'''
    cInput = customerInput.split()  #split the customer input into a variable
    quantity,index = 0,0
    item = ''
    for items in details:
        if items[1] in cInput:
            index = (cInput.index(items[1])) - 1 
            for k in range(len(quantityInWords)):
                if quantityInWords[k].upper() in cInput[index] or quantityInDigits[k] in cInput[index]:
                    quantity = int(quantityInDigits[k])
            return items[1],quantity

    
def main(time):
    '''greeting the customer and printing the items in cafe...'''
    print("...Warm greetings to our customers...")
    print("")
    print("(: Here are the items that we can serve you :)")
    mycursor.execute("SELECT cafe.ITEM_ID,cafe.ITEMS,cafe.price,cafe_inventory.CURRENT_STOCK,cafe_inventory.MIN_STOCK,\
                     cafe_inventory.REFILL_STOCK FROM cafe, cafe_inventory  WHERE cafe.ITEM_ID = cafe_inventory.ITEM_ID")
    details = mycursor.fetchall()
    for items in details:
        print(items[1])

    while time < totalTime:
    #using while loop to check if time is less than total time 
        #getting the input from user in the below format and add time 
        customerInput = input("What do u want...: ")    #input format: two coffee and 6 tea
        time += addTime 
        order = processCustomerInput(customerInput.upper(),details)   #passing userinput to a func as a arg...
        if order != None:
            mycursor.execute("SELECT ")
    # topProfitSales()    #calculating top profit and sales


main(time)