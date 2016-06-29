'''\
Rev: 1
Name: silentshadow
Description: returns the hex value of a passed decimal number
Reference: listing 6.8
Page: 186 (PDF 206)
'''

import sys


def to_hex( num):
    h1 = ( num).to_bytes( 2, byteorder='big')
    h2 = bytearray([num]).hex()
    return h1, h2
    
    
def from_hex( num):
    d1 = int.from_bytes( num, byteorder='big')
    #d2 = 
    return d1 


def main():
    n = int( input( "Give a number, e.g. 255:  "))
    d = to_hex( n)
    #h = from_hex( to_hex( n))
    print( "{} to hex is {}".format( n, d))
    #print( "{} to dec is {}".format( d, h))


if __name__ == '__main__':
    sys.exit(int(main() or 0))