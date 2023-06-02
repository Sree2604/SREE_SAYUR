############## Problem  2 #################### 
#Calculate the monthly salary for the phone salesman
#Base monthly pay Rs10000. 
#For every 5 phones sold, Rs 5000 bonus.
#For every phone aftr the first 5 phones, Rs1100 per phone bonus.
#If the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones 
# this month also, then he gets additional Rs5000.

monthlySalesList = [5,23,21,14,23,12,4,12,22,22,34,12]  # Sample number of phones sold in each month in a year
#initialise all the variables needed
basicSalary = 10000
previousMonthSalary = 0
bonus = 0

for month, phoneCount in enumerate(monthlySalesList):
    print(f"Month {month+1}")
    print(f"No of phones sold: {phoneCount}")
    #calculate the Salary using If stmts
    if phoneCount == 5:
        currentMonthSalary = basicSalary + 5000     #if he sells 5 phones then add 5000 to salary
    elif phoneCount > 5:
        additionalPhones = phoneCount - 5       #calculate no of phone exceeds 5 phone
        currentMonthSalary = basicSalary + (additionalPhones * 1100)    #multiply 1100 for each additional phones and add to salary
    else:
        currentMonthSalary = basicSalary        #otherwise salary will be 10000
    print (f"This month's salary before additional bonus {currentMonthSalary}")     #print salary before additional bonus

    #If the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones this month also
    if previousMonthSalary > 20000 and phoneCount >= 20:
        bonus = 5000    #assign bonus of 5000
    #then he gets additional Rs5000.

    if(phoneCount < 20):
        previousMonthSalary = currentMonthSalary #we set this so that, we can use this info in the next iteration
        continue #no need to calculate anything because <20 phones sold
    
    #calculate the new salary
    currentMonthSalary += bonus     #add bonus to salary 
    print(f"This month's salary after additional bonus {currentMonthSalary}")   #print salary after additional bonus
    previousMonthSalary = currentMonthSalary #assign it after add bonus to salary

"""
Output:
Month 1
No of phones sold: 5
This month's salary before additional bonus 15000
Month 2
No of phones sold: 23
This month's salary before additional bonus 29800
This month's salary after additional bonus 29800
Month 3
No of phones sold: 21
This month's salary before additional bonus 27600
This month's salary after additional bonus 32600
Month 4
No of phones sold: 14
This month's salary before additional bonus 19900
Month 5
No of phones sold: 23
This month's salary before additional bonus 29800
This month's salary after additional bonus 34800
Month 6
No of phones sold: 12
This month's salary before additional bonus 17700
Month 7
No of phones sold: 4
This month's salary before additional bonus 10000
Month 8
No of phones sold: 12
This month's salary before additional bonus 17700
Month 9
No of phones sold: 22
This month's salary before additional bonus 28700
This month's salary after additional bonus 33700
Month 10
No of phones sold: 22
This month's salary before additional bonus 28700
This month's salary after additional bonus 33700
Month 11
No of phones sold: 34
This month's salary before additional bonus 41900
This month's salary after additional bonus 46900
Month 12
No of phones sold: 12
This month's salary before additional bonus 17700
"""
