'''\
Rev: 1
Name: silentshadow
Description: Returns the max of 2 numbers 
Reference: listing 6.1
Page: 174 (PDF 194)
'''
import sys


def max( n1, n2):
    if n1 > n2:
        result = n1
    else:
        result = n2
        
    return result
    
    
def main():
    x = 5
    y = 2
    z = max( x, y)
    
    print( "The larger number of {} and {} is {}".format( x, y, z))
    
    
if __name__ == '__main__':
    sys.exit(int(main() or 0))