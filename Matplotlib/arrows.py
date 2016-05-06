'''\
Rev: 2
Author: silentshadow
Description:  experimenting with plotting and measuring distance between 2 points
Reference: https://www.youtube.com/watch?v=q7Bo_J8x_dw&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF
'''

import matplotlib.pyplot as plt
import numpy as np

plt.plot(range(10))

x1 = -50
y1 = 34

x2 = 49
y2 = -85

# Plot
plt.plot( [ x1, x2 ], [ y1, y2 ] )
plt.title( "Measuring distances")
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.show()