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

# #Get 5 marks from student and find the total
total = 0
for i in range(1,6):
    mark = int(input(f"Enter mark {i} subject: ")) #get the user input
    total = addTwoNumbers(total,mark)   #call the function to add two numbers

print(f"The student's total is: {total}")   #print the total mark 
#Call divide function to get the average
avg = divideAFromB(5,total)

print("The avg mark is ", avg)
