# ############## Problem  1 #################### 
# #Ask first friend the colors they like. Save it in a list
# #Ask another friend the same question. If the color is in the first friend's list, 
# #Print "You both like "name of the color"
# #If it is not in the first friend's list, Save it another list.
firstFriendLikes,secondFriendLikes = [],[]
print("First Friend Turn...")
print('Tell me the colors you like...')
while True:
    #ask the user to enter movies like
    colors = input().upper()
    if colors != "":
        #if the input is not empty
        firstFriendLikes.append(colors)     #append it to list 
    else:
        break       #otherwise break the loop

print("Second Friend Turn...")
print('Tell me the colors you like...')
while True:
    colors = input().upper()        #ask the another user to enter movies they like
    if colors in firstFriendLikes:
        #check the input is in firstFriendLikes list
        print(f"You both like {colors}...")     #then print that both like color name
        secondFriendLikes.append(colors)    #and append it to secondFriendLikes
    else:
        if colors == "" :
            #if the input is empty then break the loop
            break
        else:
            #otherwise append the input ot the secondFriendLike 
            secondFriendLikes.append(colors)

#print the colors liked both users
print(f"Colors liked by First Friend: {firstFriendLikes}")
print(f"Colors liked by Second Friend: {secondFriendLikes}")


"""
Output:
First Friend Turn...
Tell me the colors you like...
red
green
blue

Second Friend Turn...
Tell me the colors you like...
black
blue
You both like BLUE...
red
You both like RED...
white

Colors liked by First Friend: ['RED', 'GREEN', 'BLUE']
Colors liked by Second Friend: ['BLACK', 'BLUE', 'RED', 'WHITE']
"""