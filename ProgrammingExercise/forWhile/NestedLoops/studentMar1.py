# ######## Problem  1 ###############
# # Get and print the 2 marks each for 3 students. Also, get each studen't name
# # output should be
# # Mark 1 for Student 1 is 55
# # Mark 2 for Student 1 is 67
# # Mark 1 for Student 2 is 56 
# #etc

studentCount = 3
markCount = 2

for student in range (studentCount):
    #loop util the student reaches studentCount ie 3
    marks = []      #create a empty list to store marks
    for mark in range (1,markCount+1):
        #loop 2 times to get input for 2 marks
        inputMark = int(input(f"Enter the mark {mark} for student {student+1}: "))      #get the input for marks from user
        marks.append(inputMark)     #append it to list
    for index,mark in enumerate(marks,start=1):
        #loop until all the values in enumerated list is print
        print(f"Mark {index} for student {student+1} is {mark}")

"""
output:
Enter the mark 1 for student 1: 55
Enter the mark 2 for student 1: 74
Mark 1 for student 1 is 55
Mark 2 for student 1 is 74
Enter the mark 1 for student 2: 96
Enter the mark 2 for student 2: 25
Mark 1 for student 2 is 96
Mark 2 for student 2 is 25
Enter the mark 1 for student 3: 36
Enter the mark 2 for student 3: 85
Mark 1 for student 3 is 36
Mark 2 for student 3 is 85
"""