# ########## Program 1
# #Get an input string from the user. Add a space at every 3rd char.
# #eg input = abcdefg , output = ab cd ef g
print("")
print("PROGRAM--1")
inputString = "abcdefg"
idx = 0 #counter to track the chars
newString = ""
while idx < len(inputString):
    #loop until the counter variable less than lenght of inputString
    newString += inputString[idx]   #
    if (idx+1) % 2 == 0:
        #add space to newString if the condition is true
        newString += ' '
    idx+=1  #incrementing the index value
    
print(newString)    #print the newString

# ########## Program 2
# #Print your name in a pyramid
# #eg RAM
# #R
# #RA
# #RAM
print("")
print("PROGRAM--2")
myName = 'RAM'
outputString = ''
for letter in myName:
    outputString += letter
    print(outputString)
        

########## Program 3
#PigLatin - From the input string, for each word, remove the first, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay ythonPay
print("")
print("PROGRAM--3")
inputString = "I am Python"
pigLatinKey = 'ay'
outputString = ''
for word in inputString.split(): #gets the word in a sentence
    #take the first char
    firstChar = word[0]
    outputString += word[1:]+ firstChar + pigLatinKey + " "
print(f"Your Input String is: {inputString}")
print(f'Your Output String is: {outputString}')

########## Program 4
#PigLatin - From the input string, for each word, remove the first chars until a vowek, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay nPythoay (in Python 'o' is the first vowel)
print("")
print("PROGRAM--4")
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