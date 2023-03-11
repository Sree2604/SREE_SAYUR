'''
Encoding problem - Input is a message and a pattern. Both stringd. Output is the message writtenin the form of the pattern.
Eg -    Message - "I Love India".
        Pattern - "*** **** ** **********      *****"
        Output - "ILo veIn di aILoveIndi      aILov"
    Note how you replace each * in the pattern with the letter in the message, the space in the message doesnt matter, but the space(s) in the patterns matters.
'''

#declaring the pattern that needed in a variable
pattern = '*** **** ** **********      *****'

message = 'I Love India' # getting input from user
withoutSpaces = ""  #creating a variable to remove spaces from user input

#for loop(begin) 
for word in message:    #(removing space from user's input)
    if word != " ": 
        withoutSpaces = withoutSpaces + word    

result = ''     #declaring the variable to print the desired output

#creating an empty list and a variable n
letters = []    
n = 0
for x in withoutSpaces:     #for loop 2 begin 
    letters.append(x)       #append each letter from without spaces to the list
        
#for loop
for i in pattern:   #begin

    #if condition begin
    if i != ' ':     
        if n > (len(withoutSpaces) - 1):
            n= 0
            #adding each letter from the list for the desired output
            result = result + letters[n]
            n = n + 1   #incresing n value
        else:
            #adding each letter from the list for the desired output
            result = result + letters[n]
            n = n + 1   #incresing n value
    #if condition end
    #else begin
    else: 
        result = result + i
             
print(result)