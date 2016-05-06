'''\
Rev: 2
Name: silentshadow
Description: find runway length given airplane acceleration and take off speed
Reference: exercise 2.10
Page: 57 (PDF 77)
'''
from math import pow


def plane():
    '''\
    This is the plane function
    Formula: length = v **2 / 2 * a
    '''
    v = int( input( "Enter the speed of the aircraft:  > "))
    a = float( input( "Enter the acceleration of the aircraft:  > "))
    
    length = ( pow( v, 2) ) / ( 2 * a )
    print( "The minimum runway length needed is {.2f} meters".format( length)) 
    
    
def main():
    p = plane()
    
    
if __name__ == "__main__" : main()