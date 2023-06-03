           
######## Problem 2 ###############
#Write a program that prints out the Fibonacci sequence up to a given number.
#example 1,2,3,5,8 , next number is the sum of previous two numbers.

#get input of fibo series range
n = int(input("Enter the range of fibo seies: "))

fiboSeries = []     #define a list to store fibo series
for i in range(n):
    #loop until the range
    if i == 0:
        fiboSeries.append(i)        #if i is 0 then append it to list
    elif i == 1:
        fiboSeries.append(i)        #if i is 1 then append it to list
    else:
        #otherwise add previous two number from current index position and appenn it to list
        fiboSeries.append((fiboSeries[i-1]+fiboSeries[i-2]))    
    
print(f"Fibonacci Seies upto range of {n}")
for num in fiboSeries:
    #loop until all the values inside the list is printed..
    print(num)

"""
Output:
Enter the range of fibo seies: 8
Fibonacci Seies upto range of 8
0
1
1
2
3
5
8
13
"""