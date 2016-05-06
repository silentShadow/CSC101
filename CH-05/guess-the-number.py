'''\
Rev: 1
Name: silentshadow
Description: 
Reference: listing 5.2
Page: 137 (PDF 157)
'''

import random

num = random.randint( 0, 20)

guess = int( input( "Guess a number between 1 and 100"))

while guess != num:
    guess = int( input( "Guess a number between 1 and 100"))
    
    if guess == num:
        print( "Yup, that's the number")
    elif guess > num:
        print( "Too high")
    else:
        print( "Too low")
