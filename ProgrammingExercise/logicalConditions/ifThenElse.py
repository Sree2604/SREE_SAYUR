############# Problem 1 ###########
#Google and find the tax slabs for income tax for India. Write a program to calculate the income tax for an 
#individual. Input is Salary. Optional input - any deductions.

############ Problem 2 ####
#Calculate the BMI and if the person is underweihgt/normal/overweight/obese
#Google how to calculate BMI and decide on the input.

def calcBMI(weight,height):
    height *= 0.01 
    return round((weight / pow(height,2)),1)

print("BMI CALCULATOR")
inputWeight = float(input("Enter your Weight(in kg): "))
inputHeight = float(input("Enter your Height(in cm): "))

bmi = calcBMI(inputWeight,inputHeight)

if bmi < 18.5:
    print(f"Your BMI value is {bmi} and you are underweight...")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your BMI value is {bmi} and you are normal...")
elif bmi >= 25 and bmi < 30:
    print(f"Your BMI value is {bmi} and you are Overweight...")
else:
    print(f"Your BMI value is {bmi} and you are obese...")

########## Problem 3 ##########
##buy choc and cake
# one choc is Rs 200
# one cake is 150
#get budget from user. Also get the total number of choc and cakes that the shop has
#Hint - you can buy choc/Cake only if shop has it.

#find how many choc and cake the user can buy.

############## Problem 4 ##############
#Calculate the Grade for a student, using 3 marks.
# The student has 100 marks in any one subject, Grade is A.
# if the student has 90 or above in any one subject  Grade is B
# if the student has 60 or above in any one subject  Grade is C
# if the student has 50 or less  in all subjects  Grade is F, otherwise Grade is D.

# #Code
def calcGrade(mark1,mark2,mark3):
    if(mark1 == 100 or mark2 == 100 or mark3 == 100): #at leasr one mark is 100
        return("Grade A")
    elif ((mark1 >= 90 and mark1 < 100) or (mark2 >= 90 and mark1 < 100) or (mark3 >=90 and mark3 < 100)): 
        return("Grade B")
    elif ((mark1 >= 60 and mark1 < 90) or (mark2 >= 60 and mark1 < 90) or (mark3 >= 60 and mark3 < 90)):
        return("Garde C")
    elif ((mark1 >= 50 and mark1 < 60) or (mark2 >= 50 and mark1 < 60) or (mark3 >= 50 and mark3 < 60)):
        return("Grade F")
    else:
        return ("Grade D")

mark1 = int(input("Enter the mark of subject 1: "))
mark2 = int(input("Enter the mark of subject 2: "))
mark3 = int(input("Enter the mark of subject 3: "))

print(calcGrade(mark1,mark2,mark3))


