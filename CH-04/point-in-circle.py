'''\
Rev: 1
Name: silentshadow
Description: 
Reference: listing 4.11
Page: 118 (PDF 138)
'''

import turtle as t


# Get user values
# Opt 1: Easy but no validation
c_coords = input( "Give X, Y coords for center of circle:  >")
circ_coord = [ int( i ) for i in c_coords.split(',') ]          # Run int() over every item in c_coords splitting ','

g_coords = input( "Give X, Y coords for second point:  >")      
guess_coord = [ int( i ) for i in g_coords.split(',') ]         # Run int() over every item in g_coords splitting ','

x1 = circ_coord[0]
y1 = circ_coord[1]
r  = int( input( "Enter radius value:  >"))
x2 = guess_coord[0]
y2 = guess_coord[1]


# Opt 2: Not proficient
'''
x1 = int( input( "Enter x1 coord for center of circle:  >"))
y1 = int( input( "Enter y1 coord for center of circle:  >"))
r  = int( input( "Enter radius value:  >"))
x2 = int( input( "Enter x2 coord for second point:  >"))
y2 = int( input( "Enter y2 coord for second point:  >"))
'''

t.up()
t.goto(x1, y1)
t.down()
t.circle(r)

t.up()
t.goto(x2, y2)
t.down()
t.dot(6, 'red')


t.up()
t.goto( x1- 70, y1 - r - 20)
t.down()

dist = ( pow( (x2 - x1), 2) + pow( (y2 - y1), 2) )

if dist <= r:
    t.write( "inside", font=('arial', 20, 'normal'))
else:
    t.write( "outside", font=('arial', 20, 'normal'))
    
t.hideturtle()
t.done()
