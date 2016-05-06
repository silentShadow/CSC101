# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 10:12:57 2016

@author: jonman
@decription: turtle drawing
"""
import turtle


# Turtle motion
"""
turtle.forward(int or float)
turtle.fd(int or float)

turtle.back(int or float)
turtle.bk(int or float)
turtle.backward(int or float)

turtle.right(int or float)
turtle.rt(int or float)

turtle.left(int or float)
turtle.lt(int or float)

turtle.goto(x, y=None)
turtle.setpos(x, y=None)
turtle.setposition(x, y=None)

turtle.home()

turtle.circle(radius, extent=None, steps=None)

turtle.dot(size=None(int),color=None(str))

# Stamp a copy of the turtle shape onto the canvas
#   at the current turtle position. Return a stamp_id
#   for that stamp, which can be used to delete it by
#   calling clearstamp(stamp_id).
turtle.stamp()

turtle.position()
"""

for i in range(8):
    turtle.stamp()
    turtle.fd(30)


turtle.home()
turtle.begin_poly()
turtle.fd(100)
turtle.lt(20)
turtle.fd(30)
turtle.lt(60)
turtle.fd(50)
turtle.end_poly()
turtle.get_poly()



turtle.done()


