######## Problem 1 ###############
#write multiplication table like this
# 1 * 1 = 1
# 1 * 2 = 2
#etc. 

# Get the number and rows as input 
multiplicationNumber = int(input("Enter the multiplication number: "))
noOfEntries = int (input("How many rows do you want to print: "))

for row in range(1,noOfEntries + 1):
    # loop until the value of noOfEntries
    print(row," * ",multiplicationNumber," = ",row*multiplicationNumber)    #print the multiplication number with respective row

"""
Output:
Enter the multiplication number: 1
How many rows do you want to print: 10
1  *  1  =  1
2  *  1  =  2
3  *  1  =  3
4  *  1  =  4
5  *  1  =  5
6  *  1  =  6
7  *  1  =  7
8  *  1  =  8
9  *  1  =  9
10  *  1  =  10
"""