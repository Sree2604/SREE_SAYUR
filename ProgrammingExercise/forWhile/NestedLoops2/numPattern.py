# '''
# Program 1 - Write a program to print the following pattern.
# Input is 5 for the following pattern.
# 5 5 5 5 5 5 5 5 5
# 5 4 4 4 4 4 4 4 5
# 5 4 3 3 3 3 3 4 5
# 5 4 3 2 2 2 3 4 5
# 5 4 3 2 1 2 3 4 5
# 5 4 3 2 2 2 3 4 5
# 5 4 3 3 3 3 3 4 5
# 5 4 4 4 4 4 4 4 5
# 5 5 5 5 5 5 5 5 5
# '''

num = 5
dimension = num * 2 - 1 

for row in range(dimension):
    for column in range(dimension):
        if row == 0 or column == 0 or row == dimension - 1 or column == dimension - 1:
            print(num, end=' ')
        elif row == 1 or column == 1 or row == dimension - 2 or column == dimension - 2:
            print(num - 1, end=' ')
        elif row == 2 or column == 2 or row == dimension - 3 or column == dimension - 3:
            print(num - 2, end=" ")
        elif row == 3 or column == 3 or row == dimension - 4 or column == dimension - 4:
            print(num - 3, end=" ")
        else:
            print(num - 4, end=" ")
    print()

# '''
# Output:
# 5 5 5 5 5 5 5 5 5 
# 5 4 4 4 4 4 4 4 5 
# 5 4 3 3 3 3 3 4 5 
# 5 4 3 2 2 2 3 4 5 
# 5 4 3 2 1 2 3 4 5 
# 5 4 3 2 2 2 3 4 5 
# 5 4 3 3 3 3 3 4 5 
# 5 4 4 4 4 4 4 4 5 
# 5 5 5 5 5 5 5 5 5 
# '''