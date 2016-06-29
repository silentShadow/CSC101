'''\
Class: CSC101 Week 6
Rev: 1
Name: silentshadow
Description: this program will utilize functions to compute angles 
Reference: week 6 assignemnt B
'''

import turtle
from math import sqrt, degrees, acos, pow
from useful_turtle_functions import draw_line, draw_grid



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
    
    P = degrees( acos(( pow( p, 2) - pow( q, 2) - pow( r, 2)) / ( -2 * q * r) )) 
    Q = degrees( acos(( pow( q, 2) - pow( p, 2) - pow( r, 2)) / ( -2 * p * r) ))
    R = degrees( acos(( pow( r, 2) - pow( q, 2) - pow( p, 2)) / ( -2 * p * q) ))
    
    return P



def main():
    # to display the degree sign when printing results
    deg = u'\N{DEGREE SIGN}'

    turtle.setup(500, 500)                   # make window set size
    win = turtle.Screen()                    # refer to the screen as win
    win.title( "Triangles and Angles!")         # change the window title
    win.bgcolor( "#D3D3D3")               # change background color

    # get 3 X,Y coords from the user using eval( input())
    x1, y1, x2, y2, x3, y3 = eval( input( "Give 3 points: [e.g. 20, 20, 100, 200, 20, 200]  "))

    # compute the distances of all points
    a = distance( x1, y1, x2, y2)
    b = distance( x2, y2, x3, y3)
    c = distance( x1, y1, x3, y3)

    # round off 
    d1 = round( a * 100) / 100.0
    d2 = round( b * 100) / 100.0
    d3 = round( c * 100) / 100.0

    # make 3 seperate calls to determine_angle to find all angles opposite their sides
    angle_x = determine_angle( a,b,c)
    angle_y = determine_angle( b,c,a)
    angle_z = determine_angle( c,b,a)
    print( "The angles of the triangle are:")
    print( "\tAngle A: {:.2f}{}  \n\tAngle B: {:.2f}{}  \n\tAngle C: {:.2f}{}".format( angle_x,deg,angle_y,deg,angle_z,deg),end='\n\n')
    
    # draw the grid for the layout and referencing of plots
    draw_grid()
    draw_line( x1, y1, x2, y2, x3, y3, angle_x, angle_y, angle_z)
    
    turtle.done()



if __name__ == '__main__': main()