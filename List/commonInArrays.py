array1 = [1,3,7,9,13,14]
array2 = [1,2,7,13,15]
largeArray = []
smallArray = []
result = []
if len(array1) > len(array2):
    largeArray = array1
    smallArray = array2
else:
    largeArray = array2
    smallArray = array1

for i in largeArray:
    if i in smallArray:
        result.append(i)

print("The common values in both the array is...")
print(result)