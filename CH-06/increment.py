'''\
Rev: 2
Name: silentshadow
Description: returns the letter grade for percentile score
Reference: listing 6.
Page: 181 (PDF 201)
'''

import sys


def increment( n ):
    n += 1
    print( "\tN inside the function is {}".format( n))
    
    
def main():
    x=1
    print( "Before function call, x is {}".format( x))
    increment( x)
    print( "After function call, x is {}".format( x))
    

if __name__ == '__main__':
    sys.exit(int(main() or 0))