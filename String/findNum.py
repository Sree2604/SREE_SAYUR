def findNumbers(num):
    if num % 5 == 0 and num % 7 == 0:
        return num

print("Numbers between 1500 and 2700 that are divisible by 5 and 7")
for num in range(1500,2701):
    number = findNumbers(num)
    if number != None:
        print(number)