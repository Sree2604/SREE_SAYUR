
############## Problem 4 ##############
#Calculate the Grade for a student, using 3 marks.
# The student has 100 marks in any one subject, Grade is A.
# if the student has 90 or above in any one subject  Grade is B
# if the student has 60 or above in any one subject  Grade is C
# if the student has 50 or less  in all subjects  Grade is F, otherwise Grade is D.

# #Code

def calcGrade(mark1,mark2,mark3):
    if(mark1 == 100 or mark2 == 100 or mark3 == 100): #at leasr one mark is 100
        return "Grade A"
    elif ((90 <= mark1 < 100) or (90 <= mark2 < 100) or (90 <= mark3 < 100)): # if the student has 90 or above in any one subject  Grade is B
        return "Grade B"
    elif ((60 <= mark1 < 90) or (60 <= mark1 < 90) or (60 <= mark3 < 90)):# if the student has 60 or above in any one subject  Grade is C
        return "Garde C"
    elif ((50 <= mark1 < 60) or (50 <= mark1 < 60) or (50 <= mark3 < 60)):# if the student has 50 or less  in all subjects  Grade is F
        return "Grade F"
    else:   #otherwise Grade is D.
        return "Grade D"

# get the marks for three subjects 
mark1 = int(input("Enter the mark of subject 1: "))
mark2 = int(input("Enter the mark of subject 2: "))
mark3 = int(input("Enter the mark of subject 3: "))

grade = calcGrade(mark1,mark2,mark3) #stores the return value of calcGrade func
print(grade)    #print the grade

"""
Output:
Enter the mark of subject 1: 100
Enter the mark of subject 2: 23
Enter the mark of subject 3: 100
Grade A

Enter the mark of subject 1: 90
Enter the mark of subject 2: 32
Enter the mark of subject 3: 90
Grade B

Enter the mark of subject 1: 0
Enter the mark of subject 2: 0
Enter the mark of subject 3: 1
Grade D
"""