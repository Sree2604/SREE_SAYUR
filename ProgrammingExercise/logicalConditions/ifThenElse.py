############# Problem 1 ###########
#Google and find the tax slabs for income tax for India. Write a program to calculate the income tax for an 
#individual. Input is Salary. Optional input - any deductions.
salary = int(input("Enter ur annual salary: "))

if salary <= 300000:
    print("You need not to pay tax...")

elif 300000 < salary <= 600000:
    tax = 0.05
    print(f"You need to pay {salary * tax} from your {salary}...")

elif 600000 < salary <= 900000:
    tax = 0.10
    print(f"You need to pay {salary * tax} from your {salary}...")

elif 900000 < salary <= 1200000:
    tax = 0.15
    print(f"You need to pay {salary * tax} from your {salary}...")

elif 1200000 < salary <= 1500000:
    tax = 0.20
    print(f"You need to pay {salary * tax} from your {salary}...")

else:
    tax = 0.30
    print(f"You need to pay {salary * tax} from your {salary}...")

############ Problem 2 ####
#Calculate the BMI and if the person is underweihgt/normal/overweight/obese
#Google how to calculate BMI and decide on the input.

print("")
print("PROGRAM 2")
def calcBMI(weight,height):
    height *= 0.01  #converting the height in meters
    return round((weight / pow(height,2)),1)    #return the BMI value 

print("BMI CALCULATOR")
inputWeight = float(input("Enter your Weight(in kg): "))    #get the weight as an input
inputHeight = float(input("Enter your Height(in cm): "))    #get the height as an input

bmi = calcBMI(inputWeight,inputHeight)      #stores the return value of calcBMI func

if bmi < 18.5:  #if bmi value less than 18.5, then print the user is underweight
    print(f"Your BMI value is {bmi} and you are underweight...")
elif 18.5 <= bmi < 25:  #if bmi value more than 18.5 and less than 25 , then print the user is normal
    print(f"Your BMI value is {bmi} and you are normal...")
elif 25 <= bmi < 30:    #if bmi value more than 25 and less than 30 , then print the user is overweight
    print(f"Your BMI value is {bmi} and you are Overweight...")
else:   #otherwise print the user is obese
    print(f"Your BMI value is {bmi} and you are obese...")

########## Problem 3 ##########
##buy choc and cake
# one choc is Rs 200
# one cake is 150
#get budget from user. Also get the total number of choc and cakes that the shop has
#Hint - you can buy choc/Cake only if shop has it.

#find how many choc and cake the user can buy.
print("")
print("PROGRAM 3")
def orderQuantity(budget,itemStock,price):
    quantity,cost = 0,0     #initializing two variables
    while quantity < itemStock:     #check quantity is less than itemstock
        cost += price       #if true add the price to cost
        if cost > budget:   
            cost -= price   #if the cost greater than budget reduce price from the cost
            break   #and break the loop
        quantity += 1   #increase the quantity count
    return quantity, cost   

cakePrice, chocPrice = 150, 200     #initializing price to cake and choc and print it     
print(f"Cost of One CHOC is Rs {chocPrice}...")
print(f"Cost of One CAKE is Rs {cakePrice}...")

userBudget = int(input("Enter your budget: "))      #get the budget from the user

#enter the number of cakes and chocs that the shop has
cakeStock = int(input("How many cakes the shop has: "))     
chocStock = int(input("How many chocs the shop has: "))

if cakeStock == 0 and chocStock == 0:
    #if there is no stock on the shop...
    print("Sorry currently the shop can't serve you...")
else:
    #stores the quantity of cake and choc in a variable return by the orderQuantity func
    cakesOrder = orderQuantity(userBudget, cakeStock, cakePrice)
    chocsOrder = orderQuantity(userBudget, chocStock, chocPrice)

    #print the number of cakes and chocs the user can buy and also the cost of it...
    print(f"You can buy {cakesOrder[0]} no. of cakes from ur budget and it will cost Rs.{cakesOrder[1]}...")
    print(f"You can buy {chocsOrder[0]} no. of chocs from ur budget and it will cost Rs.{chocsOrder[1]}...")

############## Problem 4 ##############
#Calculate the Grade for a student, using 3 marks.
# The student has 100 marks in any one subject, Grade is A.
# if the student has 90 or above in any one subject  Grade is B
# if the student has 60 or above in any one subject  Grade is C
# if the student has 50 or less  in all subjects  Grade is F, otherwise Grade is D.

# #Code
print("")
print("PROGRAM 4")
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


