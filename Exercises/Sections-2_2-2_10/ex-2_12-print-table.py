'''\
Rev: 1
Author: silentshadow
Description: prints a table of numbes in three columns
Reference: exercise 2.12
Page: 58 (PDF 78)
'''
from math import pow


#
#a a^2 a^3
#1 1 1
#2 4 8
#3 9 27
#4 16 64

print("{:<10}{:<10}{}".format("a","b","a^b"))

a_list = [1,2,3,4,5]
b_list = [2,3,4,5,6]

print( "Using a dictionary to print a table")
the_dict = {1:2, 2:3, 3:4, 4:5, 5:6}
for key in the_dict:
    print( "{:<9d} {:<9d} {:d}".format(key, the_dict[ key], int(pow( key, the_dict[ key]))))
    


#print("{:<9d} {:<9d} {:d}".format(a, b, a**b))