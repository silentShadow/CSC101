from turtle import *
'''
description:  
    this program allows you to move the turtle with the arrow keys and with a,s,w,d keys
    if you ever need to find the position of the turtle just right click on the icon and the coords will show up

'''


def up():
    setheading(90)
    forward(100)

def down():
    setheading(270)
    forward(100)

def left():
    setheading(180)
    forward(100)

def right():
    setheading(0)
    forward(100)
    
def pos( x, y):
    write( position(), font=('Arial',16,'normal'))
    print( position())

listen()

onkey(up, 'Up')
onkey(down, 'Down')
onkey(left, 'Left')
onkey(right, 'Right')

onkey(up, 'w')
onkey(down, 's')
onkey(left, 'a')
onkey(right, 'd')

onclick( pos, 2)

mainloop()