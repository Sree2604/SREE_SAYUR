'''
Define a class for an employee.
Add a method to calculate the salary of the employee in that class based on the number of hrs worked.

In the main program, you are starting a new companyy. Hiring a few employees. Each one has different per hr
salary.

Get input from the owner of the company on how many hrs each employee worked.
Display the details of the employee who has the highest salary
'''

#define the employee class.
#need to have a method CalculateSalary(noOfHrsWorked)
class employee:
    empId = 0
    empName = ''
    empAge = ''
    empSalaryPerHr = 0
    empSalary = 0

    def calculateSalary(self,noOfHrsWorked):
        return self.empSalaryPerHr * noOfHrsWorked 

    def getDetails(self):
        print(f'Employee ID: {self.empId}')
        print(f'Employee Name: {self.empName}')
        print(f'Employee Age: {self.empAge}')
        print(f'Employee Salary: {self.empSalary}')
#main application

empList = []
maxSalary = 0

noOfEmployees = int(input("Enter the number of employees: "))
# #For each employee, get details from owner and store it in a list
for i in range(noOfEmployees):
    print()
    newEmployee = input("Enter the object name: ")      #get input of object name
    newEmployee = employee()       #create instance of the class

    #get input for each of class properties
    newEmployee.empName = input("enter the name of the employee: ")      
    newEmployee.empId = int(input("Enter the id of employee: "))
    newEmployee.empAge = input("Enter the age of the employee: ")
    newEmployee.empSalaryPerHr = int(input("Enter teh salary per hour(in digits): "))
    empList.append(newEmployee)      #append the instance in a list

# #For each employee, ask the no of hrs worked for the month of May.
print()
for employee in empList:
    noOfHrsWorkedInMay = int(input(f"Enter the hours {employee.empName} worked in May: "))
    salary = employee.calculateSalary(noOfHrsWorkedInMay)
    employee.empSalary = salary 
    if salary > maxSalary:
        maxSalary = salary
        empWithMaxSalary = employee

print("")
print("Employee with highest Salary")
empWithMaxSalary.getDetails()