######## Problem 3  ###############
#Write a program that prints out a diamond shape using #.
# Hint - print(5 * "$") will print  - $$$$$
# Hint - print(5* "$ ") will print  - $ $ $ $ $
n = int(input("Enter the number of rows: "))        #get the input of no of rows

# #print the top triangle
for row in range(n):
    print(" "*(n-row-1) + "# "*(row+1)) 

#print the bottom triangle
for row in range(n):
    print(" "*(row+1) + "# "*(n-row-1)) 

"""
Output:
Enter the number of rows: 5
    # 
   # # 
  # # # 
 # # # # 
# # # # # 
 # # # # 
  # # # 
   # # 
    # 
"""