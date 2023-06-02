# ########## Program 1
# #Get an input string from the user. Add a space at every 3rd char.
# #eg input = abcdefg , output = ab cd ef g

inputString = input("Enter a string: ")
idx = 0 #counter to track the chars
newString = ""
while idx < len(inputString):
    #loop until the counter variable less than lenght of inputString
    newString += inputString[idx]   #
    if (idx+1) % 2 == 0:
        #add space to newString if the condition is true
        newString += ' '
    idx+=1  #incrementing the index value
    
print(newString)    #print the newString

"""
Output:
Enter a string: abcdefg
ab cd ef g
"""