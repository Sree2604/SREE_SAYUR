'''
Write a program for a simple hotel management (no DB)
 Create a class for a hotel
 Ask the user for input and create instances
 Print which hotel has most rooms and which hotel has ratings
'''

#class definition
class hotel:
    #declare the properties of the class
    room = 0
    location = ''
    name = ''
    ratings = 0
    
"""     #create some methods for the class
    def changeName(self, newName):
        self.name = newName     

    def getName(self):
        return self.name
    
    def getLocation(self):
        return self.location """
 
#declaring some required variables
maxRooms, maxRoomHotelName = 0, ''
listOfInstance = []
maxRatings = 0

noOfHotels = int(input("Enter the no of hotels(objects): "))    #get the input of noOfHotels

for i in range(noOfHotels):
    print()
    obj = input("Enter the object name: ")      #get input of object name
    obj = hotel()       #create instance of the class

    #get input for each of class properties
    obj.name = input("enter the name of the hotel: ")      
    obj.room = int(input("Enter the no of rooms: "))
    obj.location = input("Enter the location of the hotel: ")
    obj.ratings = float(input('Enter the ratings of the hotel(in numbers): '))
    listOfInstance.append(obj)      #append the instance in a list

#loop to identify maxRooms among the instance
for eachInstance in listOfInstance:
    #check condition that instance of room is greater than maxRoom
    if eachInstance.room > maxRooms:
        maxRooms = eachInstance.room        #if true assign it as maxRoom and also the name of hotel in a variable
        maxRoomHotelName = eachInstance.name

    if eachInstance.ratings > maxRatings:
        maxRatings = eachInstance.ratings
        maxRatingsHotelName = eachInstance.name

#print the hotel name with max no of rooms and top ratings...
print(f"Hotel {maxRoomHotelName} has most no of rooms: {maxRooms}")        
print(f"Hotel {maxRatingsHotelName} has top ratings: {maxRatings}")
