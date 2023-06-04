""" 
Get the list of employee names from the user.
Get the monthly phone sales for each employee for the first 4 months of the year.
Sort the employees by name in alphabetical order and for each employee sort their phones sales in 
ascending order.

Eg - Sam, Adam, Sara
Sam's sales - 300, 567,234,1000
Adam's Sales - 340, 456,456,234
Sara' Sales - 1000,234,3000,2000

Output sample
Adam - 456,456,340,234
Sam - ...
Sara - ...
"""


employeeCount = int(input("Enter the no of employees: "))   #get the no of employee as input
noOfMonths = 4      
employeeSales = {}      #create a dictionary to store employee name and sales 

for employee in range(employeeCount):
    #loop until the count of employee
    name = input("Enter the name of the employee: ")        #get the employee name
    sales = []      #create an empty list ot store sales
    for month in range(noOfMonths):
        #loop until 4 times
        sale = int(input(f"Enter the sales in month {month+1}: "))   #get the sale of each month
        sales.append(sale)  #then append it to the sales list 
    sales.sort()    #after getting 4 month sales sort it in ascending order
    employeeSales[name] = sales     #store the sales list as value in dict with respective name of employee as key


sortedEmployeeSales = dict(sorted(employeeSales.items()))       #after collecting all employee details sort dict in alphabetical order
for name,sales in sortedEmployeeSales.items():  
    #loop until all the keys and values in dict is printed
    print(f"{name} - {sales}")

"""
Output:
Enter the no of employees: 2
Enter the name of the employee: Sree
Enter the sales in month 1: 54
Enter the sales in month 2: 95
Enter the sales in month 3: 2
Enter the sales in month 4: 20
Enter the name of the employee: Sayur
Enter the sales in month 1: 68
Enter the sales in month 2: 100
Enter the sales in month 3: 8 
Enter the sales in month 4: 45
Sayur - [8, 45, 68, 100]
Sree - [2, 20, 54, 95]
"""