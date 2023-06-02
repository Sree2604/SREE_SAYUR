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

"""
Output:
BMI CALCULATOR
Enter your Weight(in kg): 54
Enter your Height(in cm): 170
Your BMI value is 18.7 and you are normal...

BMI CALCULATOR
Enter your Weight(in kg): 40
Enter your Height(in cm): 170
Your BMI value is 13.8 and you are underweight...

Enter your Weight(in kg): 80
Enter your Height(in cm): 168
Your BMI value is 28.3 and you are Overweight...
"""