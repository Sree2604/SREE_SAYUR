'''
Check if the username and password is correct. 
     Username should contain the char @  and '.com' or '.edu' or '.tech' or 'org' at the end.
     passward is the first, third, and last 3 letters of the username followed by the first three letters of the 
     name of the company mentioned in the username, followed by any 3 numbers.
     eg username : myname@sayur.com. password - mnamesay123 
'''

#ask the user to input the username
username = input("Enter your username: ")
correctPassWord = ''     #declaring a variable to check user's password....

numbers = ['1','2','3','4','5','6','7','8','9']       #creating a list full of single digits....

if '@' in username and ('.com' in username or '.edu' in username or '.tech' in username or '.org' in username):    #condition to check user's input contain some reqirements....
     #if begin
     password = input("Enter your password: ")    #get the password from  the user
     a = username.index('@')  #get the index position of '@' form username

     #creating a correct password from username that entered by the user
     correctPassWord = username[0] +  username[2] + username[a-3] +  username[a-2] + username[a-1] +username[a+1] +  username[a+2] + username[a+3]      
     correctPassword = correctPassWord + password[-3] + password[-2] + password[-1]

     #condition to check user's password and correct password both are same
     if password[-1] in numbers and password[-2] in numbers and password[-3] in numbers and password == correctPassword :    
          print(f"Hi {username}....")   #print username    

     else:     #if the above condition is fasle
          print("Your password is wrong...")
     #if end

else:     #if the username is wrong....
    print("Username is not valid...")    
