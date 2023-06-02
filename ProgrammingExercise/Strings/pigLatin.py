
########## Program 3
#PigLatin - From the input string, for each word, remove the first, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay ythonPay

inputString = "I am Python"
pigLatinKey = 'ay'
outputString = []
for word in inputString.split(): #gets the word in a sentence
    #take the first char
    firstChar = word[0]
    outputString.append(word[1:] + firstChar + pigLatinKey)
print(f"Your Input String is: {inputString}")
print(f'Your Output String is: {" ".join(outputString)}')

"""
Output:
Your Input String is: I am Python
Your Output String is: Iay maay ythonPay
"""
