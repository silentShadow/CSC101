'''\
Rev: 2
Name: silentshadow
Description: computing angles of a triangle
Reference: listing 3.2
Page: 66 (PDF 66)
'''
import math

def angles():   
    '''\
    This is the angle computation formula
    '''
    
    # Here we are intializing the 3 coords in a dictionary
    coords = {}.fromkeys( ['x1','x2','x3','y1','y2','y3'],0)
    
    # Loop through every item in order and get new values from user
    for k in list( sorted( coords.keys())):
        coords[ k] = float( input( "Give a value for {}:  >".format( k)))
        # Print for visual confirmation
        print( k, coords[ k])
    
    # Again for visual confirmation
    print( coords)
    '''
    x1 = float( input( "Enter x1:  >"))
    x2 = float( input( "Enter x2:  >"))
    x3 = float( input( "Enter x3:  >"))
    y1 = float( input( "Enter y1:  >"))
    y2 = float( input( "Enter y2:  >"))
    y3 = float( input( "Enter y3:  >"))

    a = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
    b = math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
    c = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    '''
    
    # Pythagoran theorem: a^2 = b^2 + c^2 
    a = math.sqrt( pow( (coords.get('x2') - coords.get('x3')), 2 ) + pow( ( coords.get('y2') - coords.get('y3')),2 ))
    b = math.sqrt( pow( (coords.get('x1') - coords.get('x3')), 2 ) + pow( ( coords.get('y1') - coords.get('y3')),2 ))
    c = math.sqrt( pow( (coords.get('x1') - coords.get('x2')), 2 ) + pow( ( coords.get('y1') - coords.get('y2')),2 ))
    
    A = math.degrees( math.acos( ( pow( a, 2) - pow( b ,2) - pow( c, 2)) / ( -2 * b * c)))
    B = math.degrees( math.acos( ( pow( b, 2) - pow( a, 2) - pow( c, 2)) / ( -2 * a * c)))
    C = math.degrees( math.acos( ( pow( c, 2) - pow( b, 2) - pow( a, 2)) / ( -2 * a * b)))
    
    print( "Three angles {} {} {}".format( A, B, C))
    

def main():
    angles()
    
    
if __name__ == "__main__" : main()