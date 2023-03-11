'''
Input is an encrypted  string where there will be chars followed by number. The way to decrypt is 
to repeat the chars, by the number of times. Print the decrypted word and its length. If there are any special 
chars, all the chars between the number and special char are ignored.
 eg - ac2bd3 means acacbdbdbd. 
 ac2acc#cd3 acaccdcdcd
'''
#declared some required variables
encryptedWord = 'ac2acc#cd3'
decryptedWord = ''
letters = ''

#declared alphabets and numbers in list
alphabets = ['qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM']
numbers = ['1','2','3','4','5','6','7','8','9']

#for loop begin
for word in encryptedWord:

    for alphabet in alphabets:  
    #for loop (checking alphabets) begin

        if word in alphabet:   #if the word in list of alphabets
            # if begin
            letters = letters + word    #concatenate the word to variable "letters"
        
        elif word in numbers:   #if the word in list of numbers
            count = int(word)   #convert the word into a integer type 
            decryptedWord = decryptedWord + (letters * count)   #multiply the letters with the count and concatenate to decryptedWord
            letters = ''    #make the letters variable empty
            #if end

        else:
            letters = ''    
            continue
    #for loop (checking alphabets end)

#for loop end

#printing the encrypted, decrypted word and length of the decrypted word....
print(f'Encrypted word: {encryptedWord}')
print(f'Decrypted word: {decryptedWord}')
print(f'Length of the decrypted word: {len(decryptedWord)}')