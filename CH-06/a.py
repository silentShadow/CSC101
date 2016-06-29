'''\
Class: CSC101 Week 6
Rev: 1
Name: silentshadow
Description: this program will utilize functions to compute angles 
Reference: week 6 assignemnt B
'''

from math import sqrt, degrees, acos, pow

def distance(xa, ya, xb, yb):
    '''
    This function takes 2 points and calculates the distance between them

    The distance formula is simple:
        distance = sqrt( (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) )

     '''
    d = sqrt( pow(( xb - xa), 2 ) + pow(( yb - ya), 2) )
    return d


def determine_angle(p,q,r):
    '''
    This function calculates the inside angles of a triangle given 3 sides
    '''

    A = degrees( acos(( pow( p, 2) - pow( q, 2) - pow( r, 2)) / ( -2 * q * r) )) 
    B = degrees( acos(( pow( q, 2) - pow( p, 2) - pow( r, 2)) / ( -2 * p * r) ))
    C = degrees( acos(( pow( r, 2) - pow( q, 2) - pow( p, 2)) / ( -2 * p * q) ))

    return A, B, C



def main():
    # to display the degree sign when printing results
    deg = u'\N{DEGREE SIGN}'        

    # get 3 X,Y coords from the user using eval( input())
    x1, y1, x2, y2, x3, y3 = eval( input( "Give 3 points: [e.g. 1, 1, 6.5, 1, 6.5, 2.5]  "))

    # compute the distances of all points
    a = distance( x1, y1, x2, y2)
    b = distance( x2, y2, x3, y3)
    c = distance( x1, y1, x3, y3)

    # round off 
    d1 = round( a * 100) / 100.0
    d2 = round( b * 100) / 100.0
    d3 = round( c * 100) / 100.0

    # these values are good
    #print(a,b,c)
    #print(d1, d2, d3)

    # these both return None
    #print( determine_angle( d1, d2, d3))
    #print( determine_angle(a,b,c))

    # this too returns None
    x, y, z = determine_angle( a,b,c)
    print( "The angles of the triangle are:")
    print( "\tAngle A: {:.2f}{}  \n\tAngle B: {:.2f}{}  \n\tAngle C: {:.2f}{}".format( x,deg,y,deg,z,deg),end='\n\n')
    


if __name__ == '__main__':
    main()