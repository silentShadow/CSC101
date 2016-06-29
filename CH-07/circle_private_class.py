'''\
rev: 1
author: jonathan reiter
description: 
reference: listing 7.6
page: 227 (PDF 247)
'''

import math



class Circle:
    # constructor
    def __init__( self, radius=1): 
        self.__radius = radius              # two '_' make the var private
        
    def get_perim( self):
        return 2 * self.__radius * math.pi
        
    def get_area( self):
        return math.pi * pow( self.__radius, 2)
        
    def get_radius( self):
        return self.__radius
        
        
    
def main():
    c1 = Circle( 5)
    print()
    print( "Variable {:>23}".format( "Value"))
    print( "r {:.>30}".format( c1.get_radius()))
    print( "area {:.>27.2f}".format( c1.get_area()))
    print( "perimeter {:.>22.2f}".format( c1.get_perim()))
    print()



if __name__ == '__main__': main()