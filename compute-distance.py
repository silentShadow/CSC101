'''\
Rev: 1
Author: SilentShadow
Description:  comptue the distance between two given points and plot it
Reference: Listing 2.9
Page: 52 (PDF 72)
'''
import math, matplotlib, turtle

# Formula:
#   sqrt( (x2 - x1)**2 + (y2 - y1)**2 )

def distance():
    x1 = float(input( "enter point for x1:  " ))
    y1 = float(input( "enter point for y1:  " ))
    x2 = float(input( "enter point for x2:  " ))
    y2 = float(input( "enter point for y2:  " ))

    d = (math.sqrt( pow((x2 - x1),2) + pow((y2 - y1),2) ))
    return d
    
    
def main():
    d = distance()
    print( "Distance is {}".format(d) )
    
    
if __name__ ==  "__main__" : main()
