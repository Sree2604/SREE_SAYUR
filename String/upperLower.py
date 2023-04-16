# initialize counters for upper and lower case letters
upperCount = 0
lowerCount = 0

def countUpperLower(inputString):
    global upperCount,lowerCount
    # iterate through each character in the string
    for char in inputString:
        if char.isupper():
            upperCount += 1
        elif char.islower():
            lowerCount += 1
    
    # return the count of upper and lower case letters
    return upperCount, lowerCount

string = input("Enter a string:")
result = countUpperLower(string)

print(f"Uppercase letter count in '{string}' is {result[0]}")
print(f"Lowercase letter count in '{string}' is {result[1]}")