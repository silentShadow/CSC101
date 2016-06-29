'''\
rev: 2
author: jonathan reiter
description: 
reference: listing 7.1
page: 217 (PDF 227)
'''

import math



class Circle:
    '''
    The Circle class accepts one argument as the radius.

    It also will compute the perimeter and area of the circle based on radius passed
    '''

    # here we initialize a new objects state upon creation
    # here we initialize the data field radius with default value of 1
    def __init__( self, radius=1): 
        self.radius = radius
        
    def get_perim( self):
        return 2 * self.radius * math.pi
        
    def get_area( self):
        return math.pi * pow( self.radius, 2)
        
    def set_radius( self, radius):
        self.radius = radius


class Rectangle():
    '''
    The Rectangle class accepts two arguments as width and height

    It will compute the area and perimeter given the values passed
    '''

    # here we initialize a new objects state upon creation
    # we initialize 2 data fields with initial values 1 and 2
    def __init__(self, width=1, height=2):
        self.__width = width
        self.__height = height
    
    # instance method 1
    def get_area( self):
        return self.__width * self.__height
    
    # instance method 2
    def get_perim( self):
        return ( self.__width * 2 ) + ( self.__height * 2 )
        
    
def main():
    # this is the constructor of the Circle class 
    c1 = Circle( 5)
    print()
    print( "Circle object {:>23}".format( "Values"))
    print( "r {:.>35}".format( c1.radius))
    print( "area {:.>32.2f}".format( c1.get_area()))
    print( "perimeter {:.>27.2f}".format( c1.get_perim()))
    print()

    r1 = Rectangle(2, 5)
    print()
    print( "Rectangle object {:>20}".format( "Values"))
    print( "area {:.>32}".format( r1.get_area()))
    print( "perim {:.>31}".format( r1.get_perim()))
    print()



if __name__ == '__main__': main()