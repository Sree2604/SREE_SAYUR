#write code for both for and while loop
#Get marks from 5  students and calculate avg
#

#for loop
total = 0
noOfStudents = 100
for studentNo in range(1,noOfStudents+1,5):
    mark = int(input(f"Enter the mark of student {studentNo}: "))
    total += mark
print("Avg is ",total/noOfStudents)

#using while loop
total = 0
studentNo = 1
interval = 5
while (studentNo < noOfStudents):
    mark = int(input(f"Enter the mark of student {studentNo}: "))
    total += mark
    studentNo += interval
print ("Avg is ",total/noOfStudents)