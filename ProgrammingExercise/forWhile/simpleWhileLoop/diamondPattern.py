# ######## Problem 1 ###############
# #Write a program that prints out a diamond shape using $.
# #After printing each line, wait for user input. If the user presses space, continue
# #If the users presses any other key, stop printing. Maximum 10 lines
def topTriangle(n):
    #print the top triangle
    print(" "*((height//2)-n-1) + "$ "*(n+1))

def bottomTriangle(m):
    #print the bottom triangle
    print(" "*(m+1) + "$ "*((height//2)-m-1)) 

#decalring some required variables
count,n,m = 0,0,0
height = 10

#get the input from user to print diamond
userInput = input("Press space to continue...")
while count < height and userInput == ' ':
    #loop until the userIput is 'space' and count less than height
    if n < (height//2):
        #if n is less than half of height call func to print topTriangle
        topTriangle(n)  
        n += 1      #increment the n value
    else: 
        #otherwise call func to print bottomTriangle
        bottomTriangle(m)       
        m+=1       #increment the m value
    
    userInput = input()     #get the userInput again
    count+=1        #and increase the count value

"""
Output:
Press space to continue... 
    $ 
 
   $ $ 
 
  $ $ $ 
 
 $ $ $ $ 
 
$ $ $ $ $ 
 
 $ $ $ $ 
 
  $ $ $ 
 
   $ $ 
 
    $ 
  
Press space to continue... 
    $ 
 
   $ $ 
 
  $ $ $ 
 
 $ $ $ $ 
 
$ $ $ $ $ 
 
 $ $ $ $ 
f
"""