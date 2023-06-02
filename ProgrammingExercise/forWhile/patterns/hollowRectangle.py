#Write code for drawing these patterns.
#Get width and length from the user.
# draw a empty rectangle woth char *
#eg 
'''
Row 5, col 7
* * * * * * *
*           *
*           *
*           *
* * * * * * *

'''
#get width and length from user 
widthSize = int(input("Enter the width of rectangle: "))
lengthSize = int(input("Enter the length of rectangle: "))

for width in range(widthSize):
    for length in range(lengthSize):
        if width == 0 or width == widthSize - 1 or length == 0 or length == lengthSize - 1:
            #if width or length double equals 0 or max size then print "*"
            print("*",end=" ")
        else:
            #otherwise print blaxk space
            print(" ", end=" ")
    print()     #for each row it should be in new line 

"""
Output:
Enter the width of rectangle: 5
Enter the length of rectangle: 7
* * * * * * * 
*           * 
*           * 
*           * 
* * * * * * * 
"""