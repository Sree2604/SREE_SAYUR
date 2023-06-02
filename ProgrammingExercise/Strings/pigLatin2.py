########## Program 4
#PigLatin - From the input string, for each word, remove the first chars until a vowek, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay nPythoay (in Python 'o' is the first vowel)

inputString = "I am Python"
pigLatinKey = 'ay'
vowels = ['a','e','i','o','u']
outputString = ''

for word in inputString.split(): #gets the word in a sentence
    firstVowelIndex = 0
    firstChar = word[0]
    for index, char in enumerate(word): #returns both the index and the char in the word
        if char in vowels:
            firstVowelIndex = index #assigning index value to a variable
            
    if firstVowelIndex != 0:
        outputString += word[firstVowelIndex + 1:] + word[:firstVowelIndex] + word[firstVowelIndex] + pigLatinKey + " "
    else:
        outputString += word[1:]+ firstChar + pigLatinKey + " "

print(f"Your Input String is: {inputString}")
print(f'Your Output String is: {outputString}')

"""
Output:
Your Input String is: I am Python
Your Output String is: Iay maay nPythoay 
"""