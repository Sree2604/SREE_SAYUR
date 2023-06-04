# #Fill in the missing code whereever it says #FillinMissingCode
# #Fix the syntax errors as needed.

# #This is code has functions for basic arithmetic operations. Add, subtract, multiply and divide
# #add new functions as needed.

# #The main functions is to find the total profit

def addTwoNumbers(a, b):
    ans = a + b     #add two nums
    return ans

def subtractAfromB(a, b):
    ans = b - a    #sub a from b
    return ans

def multiplyTwoNumbers(a,b):
    ans = a * b     #multipy the two nums
    return ans

def divideAFromB(a, b):
    ans = b / a     #divide a from b
    return ans

# #main code


# #we have sales data for a week. 
costOfCoffee, costOfTea, costOfVadai = 25,20,25

# employeeSalary = 500 #Rs500 per day

coffeeSales = [56,78,56,45,90,103,120]
teaSales = [100,123,456,123,222,400,346]
vadaiSales = [23,45,67,12,89,90,120]

# #Find total sales in the week.
def totalSales(itemSales):
    total = 0
    for sale in itemSales:
        total = addTwoNumbers(sale,total)
    return total

totCoffeeSales = totalSales(coffeeSales)
totTeaSales = totalSales(teaSales)
totVadaiSales = totalSales(vadaiSales)

# #calculate avg sales for a week
avgCoffeeSales = divideAFromB(len(coffeeSales),totCoffeeSales)
avgTeaSales = divideAFromB(len(teaSales),totTeaSales)
avgVadaiSales = divideAFromB(len(vadaiSales),totVadaiSales)

print(f"Total sales of Coffee is {totCoffeeSales}")
print(f"Total sales of Tea is {totTeaSales}")
print(f"Total sales of Vadai is {totVadaiSales}")

print(f"Avg sales of Coffee is {round(avgCoffeeSales,2)}")
print(f"Avg sales of Tea is {round(avgTeaSales,2)}")
print(f"Avg sales of Vadai is {round(avgVadaiSales,2)}")

# #calculate profit.


 



