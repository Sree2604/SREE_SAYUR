# ########## Program 1
# #find the list unique words in a sentence
# #hint - Each word is a key, count is the value

sentence = "This is a cat and it has a tail and two eyes"
countOfWords = {}   #declaring a dictinary
for word in sentence.split():
    #loop the sentence of each word by split it into a list
    if word not in countOfWords:
        countOfWords[word] = 1  #add the word and its count 
    else:
        countOfWords[word] += 1 #increasing the count of word

print("The given sentence contains: ")
for word,count in countOfWords.items(): 
    #print the word and count from the dict
    print(f"{word} : {count}")

"""
Output:
The given sentence contains: 
This : 1
is : 1
a : 2
cat : 1
and : 2
it : 1
has : 1
tail : 1
two : 1
eyes : 1
"""