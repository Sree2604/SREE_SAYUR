char = ''
charOccurance = {} #keyword is the char and value is the count of the char
while (char.lower() != 'z'):
    char = input("Enter a character: ")

    if char in charOccurance:
        charOccurance[char] += 1
    else:
        charOccurance[char] = 1

print(charOccurance)