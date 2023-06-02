
# ############## Problem 2 ####################
# #Ask the user how many members in the family. Get Name, age and height and weight.
# #add the details into four lists.
# #Print the each memeber of the family and their details
# #eg output 
# # Name      Age     Height(cm)      Weight(kg)
# # Ram       35      180             80
# # Seetha    34      145             58
# #

#initalizing some necessary list and variables
nameList, ageList = [], []
heightList, weightList = [], []
member = 1
noOfPeople = int(input("How many people in the family: "))      #get the input of no of family members
while member <= noOfPeople:     #loop until noOfPeople
    details = input(f"Enter the details of member {member} Name, age, height(in cm), weight(in kg): ")  #get the input of necesary details from user for each family member
    x = details.rsplit(',')     #split the user details and save it in list
    if len(x) == 4:
        #check the length of list is 4 then append each details into respective list
        nameList.append(x[0])
        ageList.append(x[1])
        heightList.append(x[2])
        weightList.append(x[3])
        member += 1     #increase the count of member
    else:
        #otherwise ask the user to input again
        print("Enter all required details...")
        continue
# #print the header 
print ("Name\t\tAge\t\tHeight(cm)\t\tWeight(kg)") #learn about \t
for index, member in enumerate(nameList): #Learn how enumerate works
    print( f"{member}\t\t{ageList[index]}\t\t{heightList[index]}\t\t\t{weightList[index]}")


"""
Output:
How many people in the family: 2
Enter the details of member 1 Name, age, height(in cm), weight(in kg): Ram,35,180,80
Enter the details of member 2 Name, age, height(in cm), weight(in kg): Seetha,34,145,58
Name            Age             Height(cm)              Weight(kg)
Ram             35              180                     80
Seetha          34              145                     58
"""