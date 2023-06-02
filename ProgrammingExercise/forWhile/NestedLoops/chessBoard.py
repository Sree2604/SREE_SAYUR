# ######## Problem  3 ###############
# #Print Chess board (alternate black and white squares)
# #print('\u25A0') - will print white Square. You can use "B" to print black squares
dimension = 8   #declaring dimension of chess board

for row in range(dimension):        
    for column in range(dimension):
        if (row + column) % 2 == 0: #if the sum of row and column is even then print white box
            print('\u25A0',end =" ")
        else:
            #otherwise print "b"
            print('B',end =" ")
    print()     #after completing each row print new line

"""
Output:
■ B ■ B ■ B ■ B 
B ■ B ■ B ■ B ■ 
■ B ■ B ■ B ■ B 
B ■ B ■ B ■ B ■ 
■ B ■ B ■ B ■ B 
B ■ B ■ B ■ B ■ 
■ B ■ B ■ B ■ B 
B ■ B ■ B ■ B ■ 
"""