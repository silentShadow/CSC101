'''\
Rev: 1
Name: silentshadow
Description: drawing simple shapes with turtle
Reference: listing 3.5
Page: 82 (PDF 92)

home() sets turtle back to original position
dot(3,color='red')
square
speed()
undo()
'''

import turtle as t

t.pensize(3)
t.up()                  # Lift the pen up
t.goto(-200, -50)       # X, Y coords
t.down()
t.circle(40, steps=3)   # 3 steps means a triangle

t.up()
t.goto(-100, -50)
t.down()
t.circle(40, steps=4)    # Square

t.up()
t.goto(0, -50)
t.down()
t.circle(40, steps=5)   # Pentagon

t.up()
t.goto(100, -50)
t.down()
t.circle(40, steps=6)   # Hexagon

t.done()