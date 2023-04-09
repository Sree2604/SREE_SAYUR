'''
THere are two arrays of numbers. the numbers are sorted in ascending order. 
Find the numbers that are common in both arrays. 
Eg - array 1 = [1,3,7,9,13,14], array2 [1,2,7,13,15]. answer - [1,7,13]
'''
array1 = [1,3,7,9,13,14]
array2 = [1,2,7,13,15]

largeArray = []
smallArray = []

if len(array1) > len(array2):
    largeArray = array1
    smallArray = array2
else:
    largeArray = array2
    smallArray = array1

print("The common values in both the array is...")
for i in largeArray:
    if i in smallArray:
        print(f'{i}')