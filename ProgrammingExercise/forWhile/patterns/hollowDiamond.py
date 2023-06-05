
# next pattern is - empty diamond
n = int(input("Enter the height of diamond: "))

mid = n//2      #identifying the mid value 

for row in range(n):        
    for col in range(n):
        if ((row+col)==mid) or ((col-row)==mid) or ((row-col)==mid) or ((row+col)==mid+(n-1)):
            #check the condition and print "*" in specified position
            print("*",end="")
        else:
            #otherwise print space
            print(" ",end="")
    print()     #after completing 