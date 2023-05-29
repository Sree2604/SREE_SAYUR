# #Fill in the missing code whereever it says #FillinMissingCode
# #Fix the syntax errors as needed.

# #This is code has functions for basic arithmetic operations. Add, subtract, multiply and divide
# #The main function adds all student marks and finds the average

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
 
marksInMaths = [56,78,56,45,90]
mathsTotal = 0
for i in marksInMaths:
    mathsTotal = addTwoNumbers(i,mathsTotal) #calculate the total 
mathsAvg = divideAFromB(len(marksInMaths),mathsTotal)   #calculate the avg
print(f"Avg mark in Maths: {mathsAvg}")

marksInScience = [90,78,67,8,98]
scienceTotal = 0
for i in marksInScience:
    scienceTotal = addTwoNumbers(i,scienceTotal)    #calculate the total 
scienceAvg = divideAFromB(len(marksInScience),scienceTotal) #calculate the avg
print(f"Avg mark in Science: {scienceAvg}")

marksInHistory = [87,44,56,34,90]
historyTotal = 0
for i in marksInHistory:
    historyTotal =addTwoNumbers(i,historyTotal) #calculate the total 
historyAvg = divideAFromB(len(marksInHistory),historyTotal) #calculate the avg
print(f"Avg mark in History: {historyAvg}")

