'''\
Rev: 1
Name: silentshadow
Description: 
Reference: listing 5.1
Page: 136 (PDF 156)
'''

import random


num1 = random.randint( 0, 9)
num2 = random.randint( 0, 9)

if num1 < num2:
    num1, num2 = num2, num1
    
answer = int( input( "What is {} - {}  >".format( num1, num2)))

while num1 - num2 != answer:
    answer = int( input ( "Incorrect answer. Try again. \n{} - {} is  >".format( num1, num2)))
    
print( "Correct")