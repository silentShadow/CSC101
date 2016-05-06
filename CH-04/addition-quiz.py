'''\
Rev: 1
Name: silentshadow
Description: 
Reference: listing 4.1
Page: 94 (PDF 114)
'''

import random

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)

real_answer = int( num1 + num2)
user_answer = int( input( "What is {} + {}?  >".format( num1, num2)))

if user_answer == real_answer:
    print( "Correct")
else:
    print( "Incorrect")



print( user_answer)