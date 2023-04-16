def fizz(num):
    """This function takes num as arg and checks the passed arg is divisible by 3 then returns 'Fizz'"""
    if num % 3 == 0:
        return "Fizz"
def buzz(num):
    """Same as above function, checks the passed arg is divisible by 5 then returns 'Buzz'"""
    if num % 5 == 0:
        return "Buzz"
def fizzBuzz(num):
    """Same as above functions, checks the passed arg is divisible by 3 and also divisible by 5 then returns 'FizzBuzz'"""
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"

for num in range(1,51):
    '''This for loop iterates over 1 to 50 and also checks through three defined functions
    if any one of the function returns a value but not None it print the value. Otherwise print thr num itself'''
    if fizzBuzz(num) != None:
        print(f"{fizzBuzz(num)}")
    elif fizz(num) != None :
        print(f"{fizz(num)}")
    elif buzz(num) != None:
        print(f"{buzz(num)}")
    else:
        print(f"{num}")