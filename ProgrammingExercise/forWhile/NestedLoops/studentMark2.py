    
# ######### Problem 1.1
# #same problem as above, but output should have the student name and all the marks in the same line.
# # Eg - Input - Student Name - Chitra, Mark1 1 55, Mark 2 67
# #output -  Chitra's marks 55, 67

studentCount = 3
markCount = 2

for student in range (studentCount):
    #loop util the student reaches studentCount ie 3
    studName = input("\nEnter the student name: ")
    marks = []      #create a empty list to store marks
    for mark in range (1,markCount+1):
        #loop 2 times to get input for 2 marks
        inputMark = int(input(f"Enter the mark {mark} for student {studName}: "))      #get the input for marks from user
        marks.append(inputMark)     #append it to list
    print(f"{studName}'s marks", end=" ")
    for mark in marks:
        #loop until all the values in list is print
        print(mark,end=" ")

"""
Output:
Enter the student name: Sree  
Enter the mark 1 for student Sree: 55
Enter the mark 2 for student Sree: 75
Sree's marks 55 75 
Enter the student name: Sayur  
Enter the mark 1 for student Sayur: 85
Enter the mark 2 for student Sayur: 72
Sayur's marks 85 72
Enter the student name: Abc 
Enter the mark 1 for student Abc: 45
Enter the mark 2 for student Sree: 68
Abc's marks 45 68 
"""