'''\
Rev: 1
Name: silentshadow
Description: 
Reference: listing 6.6
Page: 183 (PDF 203)
'''

import sys
from gcd_Function import *


n1 = int( input( "1st:  "))
n2 = int( input( "2nd:  "))

print( "GCD for {} and {} is {}".format( n1, n2, gcd( n1, n2)))