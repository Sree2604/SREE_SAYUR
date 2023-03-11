'''
Write an app for the fruit vendo. Fruit vendor has a lists of fruits (apple, orange, banana, etc) When the customer comes in, vendor asks "What do u want to buy?".
The customer say "I want an apple", or "Apple" or "Three apple" or something like that .
Your program will find out what fruit the customer is asking.
Your program will also find, if the customer say the quantity, If not, ask him how much he wants.
'''
#print list of fruits for the customers
print("Welcome to the fruit shop...")
print("")
print("Lists of fruits:\n1.Apple \n2.Orange \n3.Banana")
print("")
print("What do you want to buy...?") #print when customer comes inside shop

fruit = ""
quantity = 0

twoDigits= ['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninty']

customerRequest = input("Enter what do you want to buy: ").lower()

if 'orange' in customerRequest:
    fruit = 'orange'
elif 'apple' in customerRequest:
    fruit = 'apple'
elif 'banana' in customerRequest:
    fruit = 'banana'
else:
    print('Sorry we do not have that fruit....')

if customerRequest not in twoDigits:
    if 'one' in customerRequest or '1' in customerRequest:
        quantity = 1

    elif 'two' in customerRequest or '2' in customerRequest:
        quantity = 2

    elif 'three' in customerRequest or '3' in customerRequest:
        quantity = 3

    elif 'four' in customerRequest or '4' in customerRequest:
        quantity = 4

    elif 'five' in customerRequest or '5' in customerRequest:
        quantity = 5

    elif 'six' in customerRequest or '6' in customerRequest:
        quantity = 6

    elif 'seven' in customerRequest or '7' in customerRequest:
        quantity = 7

    elif 'eight' in customerRequest or '8' in customerRequest:
        quantity = 8

    elif 'nine' in customerRequest or '9' in customerRequest:
        quantity = 9

else:
    if quantity == 0:
        print("Please tell me the quantity in single digit...")
        quantity = int(input("Enter the quantity in numbers: "))
        print("")
        print("Only single digit amount of quantity we have....")
        print("")
        quantity = 0
        quantity = int(input("Enter the quantity in numbers: "))
        
if fruit != "":
    if quantity > 1:
        print(f"The customer asked {quantity} number of {fruit}s")
    else:
        print(f"The customer asked only {quantity} {fruit}")
    print("Thank you :)")
    
else:
    print("The customer did not buy any fruit :(")