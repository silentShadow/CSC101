'''\
Rev: 1
Name: silentshadow
Description: drawing simple shapes with turtle
Reference: listing 3.6
Page: 83 (PDF 103)

color("red")
begin_fill()
end_fill()
hideturtle()
'''

import turtle as t

# Triangle
t.pensize(3)
t.up()
t.goto(-200, -50)
t.down()
t.begin_fill()
t.color("red")
t.circle(40, steps=3)
t.end_fill()

# Square
t.up()
t.goto(-100, -50)
t.down()
t.begin_fill()
t.color("blue")
t.circle(40, steps=4)
t.end_fill()

# Pentagon
t.pensize(3)
t.up()
t.goto(0, -50)
t.down()
t.begin_fill()
t.color("red")
t.circle(40, steps=5)
t.end_fill()

# Hexagon
t.up()
t.goto(100, -50)
t.down()
t.begin_fill()
t.color("blue")
t.circle(40, steps=6)
t.end_fill()

# Fill in all of the shapes
t.up()
t.goto(200, -50)
t.down()
t.begin_fill()
t.color("purple")
t.circle(40)
t.end_fill()
t.color("green")
t.up()
t.goto(-100, 50)
t.down()

t.write("Cool, colorful shapes", font=("Times",18,"bold"))
t.hideturtle()

t.done()