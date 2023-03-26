Input = 'sabcyursdfsb'

def findC(Input):
    index1 = Input.find('c')
    index2 = Input.rfind('c')
    if index1 != -1 and index2 != -1:
        if index1 == index2:
            print("There is only one 'c' in the string...")
        else:
            print(Input[index1+1:index2])
    else:
        print("There are no letters a,b and c in the given input")

def findB(Input):
    index1 = Input.find('b')
    index2 = Input.rfind('b')
    if index1 != -1 and index2 != -1:
        if index1 == index2:
            print("There is only one 'b' in the string...")
            findC(Input)
        else:
            print(Input[index1+1:index2])
    else:
        findC(Input)

def findA(Input):
    index1 = Input.find('a')
    index2 = Input.rfind('a')
    if index1 != -1 and index2 != -1:
        if index1 == index2:
            print("There is only one 'a' in the string...")
            findB(Input)
        else:
            print(Input[index1+1:index2])
    else:
        findB(Input)

findA(Input)