'''\
Rev: 1
Name: silentshadow
Description: this is the module for the random char geneation
Reference: listing 6.11
Page: 191 (PDF 212)
'''

from random import randint


def rand_char( ch1, ch2):
    return chr( randint( ord( ch1), ord( ch2)))
    
    
def rand_lower():
    return rand_char( 'a', 'z')
    
    
def rand_upper():
    return rand_char( 'A', 'Z')
    
    
def rand_digit():
    return rand_char( '0', '9')

    
def rand_ascii():
    return chr( randint( 0, 127))
