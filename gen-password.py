'''\
rev: 1
author: silentshad0w
description: generate a strong password of random dictionary words
reference:  None
'''
import os.path
from random import randint

words = []
passwd = []
your_passwd = ""



if not os.path.isfile('dictionary.txt'):
    print( "File doesn't exist idiot!" )
else:
    # The dictionary file has the words
    with open( 'dictionary.txt', 'r') as fh:
        #print( fh.read( 100))
        reader = fh.read().splitlines()
        for word in reader:
            words.append( word)
            


count = 0
while count < 5:
    passwd.append( words[ randint( 1, ( len( words) - 1)) ] )
    count += 1
    


for i in passwd:
    your_passwd += i.capitalize()
    
    
print( "Since you can't create a random password here is one for you: \n\t{}".format( your_passwd))