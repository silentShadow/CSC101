'''\
Rev: 1
Name: silentshadow
Description:
Reference: exercise 2.2
Page: 55 (PDF 75)
'''
from math import pi, pow


def volume():
    r = float(input( "Enter radius of cylinder  " ))
    length = float(input( "Enter length of cylinder  " ))

    area = pi * pow(r, 2)
    vol = area * length
    
    print( "Area is {}".format(area) )
    print( "Volume is {}".format(vol) )
    return area, vol


def main():
    v = volume()
    
    
if __name__ == "__main__" : main()