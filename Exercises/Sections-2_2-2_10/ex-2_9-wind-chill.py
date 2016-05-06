'''\
Rev: 6
Name: silentshadow
Description: calculate the wind chill temp
Reference: exercise 2.9
Page: 57 (PDF 77)
'''
from math import pow


def wind():
    '''\
    This is the wind chill function
    Formula: Twc = 35.74 + .06215Ta - 35.75V ** 0.16 + .4275TaV ** 0.16
    Ta = outside temp in F
    V = wind spees in MPH
    Twc = wind chill temp
    '''
    V = int( input( "Enter the wind speed in MPH (Not less than 2 MPH)  >"))
    while V < 2:
        V = int( input( "Must be above 2 MPH  >"))
        
    Ta = float( input( "Enter the temperature in F degrees (-58 to 41)  >"))
    while Ta < -58.0 and Ta > 41.0:
        Ta = float( input( "Must be between -58 and 41 F  >"))
        
    Twc = 35.74 + ( 0.6215 * Ta ) - (35.75 * pow( V, .16)) + (0.4275 * Ta * pow( V, .16))
    print( "The wind chill index is {:.2f}".format( Twc))
    
    
def main():
    w = wind()
    
    
if __name__ == "__main__" : main()