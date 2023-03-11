'''
Print the level of the password security and if the password is acceptable
    Weak - only alphabets or only numbers or only special chars
    Ok - at least one alphabet, one number and one special char
    strong - at least three alphabets, two numbers and one special char
    Very strong - same as strong, but at least 16 count

'''
#getting password from the user as input
password = input("Enter the password (minimum 8 characters): ")

#declaring some variables
alphabets_count = 0
special_characters_count = 0
numbers_count = 0

length_of_password = len(password) #calculating length of the password

#creating some set of lists
alphabets = ['qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM']
numbers = ['0123456789']
special_characters = ['!@#$%^&*()_+-=']

#if length is greater than 8
if length_of_password >= 8: #if begin
    
    for i in password: #using for loop checking each character with abovee lists
        for alphabet in alphabets:
            if i in alphabet:
                alphabets_count = alphabets_count + 1
        for number in numbers:
            if i in number:
                numbers_count = numbers_count + 1
        for special_character in special_characters:
            if i in special_character:
                special_characters_count = special_characters_count + 1

    if alphabets_count >=3 and numbers_count >=2 and special_characters_count >=1:
        if length_of_password >= 16:
            print("Your password is very strong...")
        else:
            print("Your password is strong...")

    elif alphabets_count == length_of_password or numbers_count == length_of_password or special_characters_count == length_of_password:
        print("Your password is weak...")

    elif alphabets_count >= 1 or numbers_count >= 1 or special_characters_count >= 1:
        if alphabets_count >= 1 and numbers_count >=1 and special_characters_count >= 1:
            print("Your password is ok...")
        else:
            print("Your password is more than ok...")
   
else:
    print("Your password should be minimum of 8 characters")