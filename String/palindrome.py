""" def isPalindrome(string):

    if len(string) < 2:
        return True
    elif string[0] == string[-1]:
        return isPalindrome(string[1:-1])
    else:
        return False

inputString = input("Enter a string: ")
if isPalindrome(inputString):
    print("It is a palindrome...")
else:
    print("It is not a palindrome...") """

def checkPalindrome(string):
    start = 0
    end = len(string)-1
    while(start<end):
           if(string[start] == string[end]):
               start = start + 1
               end = end - 1
           else:
               return False
    return True

inputString = input("Enter the string: ")
if checkPalindrome(inputString):
    print("It is a palindrome...")
else:
    print("It is not a palindrome...")