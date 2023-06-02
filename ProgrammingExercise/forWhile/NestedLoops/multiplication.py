
# ######## Problem  2 ###############
# #Print multiplication tables from 7 to 16, each number upto 12 rows.
noOfRows = 12
for multiplicationNum in range(7,17):       #loop from 7 to until 16
    print(" ") 
    print(f"Multiplication Table of {multiplicationNum}")
    for row in range(1,noOfRows+1):     #loop upto 12 rows
        print(f"{row} * {multiplicationNum} = {row * multiplicationNum}", end="; ")
    print(" ") 

