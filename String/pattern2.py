'''
7. Same as above, but the pattern can be multi line.
Eg 
Message - "I Love India".
Pattern - 
'This is 
          a 
             Test'
Output  -
'ILov eI 
          n
             diaI'

'''
#declaring the pattern that needed in a variable
pattern = """This is          a             Test
"""


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