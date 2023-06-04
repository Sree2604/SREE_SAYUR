############# Problem 1 ###########
#Google and find the tax slabs for income tax for India. Write a program to calculate the income tax for an 
#individual. Input is Salary. Optional input - any deductions.

print("Tax Slab Details")
print()
print("Up to Rs. 3,00,000 \t\tNil \
\nRs. 3.00,000 to Rs. 6,00,000	5% on income which exceeds Rs. 3,00,000 \
\nRs. 6,00,000 to Rs. 900,000	Rs. 15,000 + 10% on income more than Rs. 6,00,000\
\nRs. 9,00,000 to Rs. 12,00,000	Rs. 45,000 + 15% on income more than Rs. 9,00,000\
\nRs. 12,00,000 to Rs. 1500,000	Rs. 90,000 + 20% on income more than Rs. 12,00,000\
\nAbove Rs. 15,00,000	Rs. 150,000 + 30% on income more than Rs. 15,00,000")
print()

salary = int(input("Enter ur annual salary: "))

if salary <= 300000:
    print("You need not to pay tax...")

elif 300000 < salary <= 600000:
    tax = 0.05
    print(f"You need to pay {(salary * tax)} from your {salary}...")

elif 600000 < salary <= 900000:
    tax = 0.10
    print(f"You need to pay {(salary * tax) + 15000} from your {salary}...")

elif 900000 < salary <= 1200000:
    tax = 0.15
    print(f"You need to pay {(salary * tax) + 45000} from your {salary}...")

elif 1200000 < salary <= 1500000:
    tax = 0.20
    print(f"You need to pay {(salary * tax) + 90000} from your {salary}...")

else:
    tax = 0.30
    print(f"You need to pay {(salary * tax) + 150000} from your {salary}...")

