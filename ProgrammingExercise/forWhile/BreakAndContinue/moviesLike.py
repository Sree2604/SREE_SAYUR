# ############## Problem  1 #################### 
# #Ask first friend the movies they like. Save it in a list
# #Ask another friend the same question. If the movie is in the first friend's list, 
# #Print "You both like "name of the color"
# #Continue until they is atleast 3 movies they both like

commonMovieCount = 0
commonMovies = []
firstFriendLikes = []       #creating a empty list
print("First Friend Turn...")
while True:
    #ask the user to enter movies like
    movie = input('Tell me the movies you like...').lower()
    if movie != "" or movie != " ":
        #if the input is not empty
        firstFriendLikes.append(movie)      #append it to list 
    else:
        break       #otherwise break the loop
print("Second Friend Turn...")
while commonMovieCount < 3:
    movie = input("Tell me the movie u like...").lower()        #ask the another user to enter movies they like
    if movie not in commonMovies:   
        #if the input is not in commonMovies list...
        if movie in firstFriendLikes:
            #if the input is in movies list liked by first person
            commonMovieCount += 1       #then increase commonMovieCount
            commonMovies.append(movie)  #append it to the commonMovieList
            print(f"You both like {movie}...")      
        else:
            #otherwise continue
            print("Try Again...")
            continue
    else:
        #if already in commonMovie list then ask the user to input again...
        print("You already told this...")

"""
Output:
First Friend Turn...
Tell me the movies you like...avatar
Tell me the movies you like...ghosted
Tell me the movies you like...inception
Tell me the movies you like...
Second Friend Turn...
Tell me the movie u like...sfgag
Try Again...
Tell me the movie u like...fdaf
Try Again...
Tell me the movie u like...avatar
You both like avatar...
Tell me the movie u like...ghosted
You both like ghosted...
Tell me the movie u like...skjghos
Try Again...
Tell me the movie u like...skjdfhwh
Try Again...
Tell me the movie u like...inception
You both like inception...
"""