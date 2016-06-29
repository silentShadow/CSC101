'''\
Rev: 1
Name: silentshadow
Description: 
Reference: listing 6.14
Page: 200 (PDF 220)
'''

from turtle import *


# Draw XY plane
def draw_grid():
    speed( 0)
    pencolor( "#5F9EA0")

    # Set positive Y plane
    setheading( 90)
    write("0", align="right", font=("Arial",10,"normal"))
    for i in range(0,11):
        dot(size=4)
        write(i*20, align="right", font=("Arial",10,"normal"))
        forward( 20)

    # Set negative Y plane
    home()
    setheading( 270)
    for i in range(0,11):
        dot(size=4)
        write(i*20, font=("Arial",10,"normal"))
        forward( 20)

    # Set positive X plane
    home()
    setheading( 0)
    for i in range(0,11):
        dot(size=4)
        write(i*20, font=("Arial",10,"normal"))
        forward( 20)
        
    # Set negative X plane
    home()
    setheading( 180)
    for i in range(0,11):
        dot(size=4)
        write(i*20, font=("Arial",10,"normal"))
        forward( 20)

    home()
        


# Draw a line
def draw_line( x1, y1, x2, y2, x3, y3, angle_a, angle_b, angle_c):
    deg = u'\N{DEGREE SIGN}'
    hideturtle()
    pencolor( "#A52A2A")
    speed( 0)
    up()

    # plot the first set of XY coords
    goto( x1, y1)
    dot( size=4)
    write( "Angle Q: ", True, font=("Arial", 12, "normal"))
    write( round(angle_b * 100) / 100.0, True, font=("Arial", 12, "normal"))
    write( deg, True, font=("Arial", 12, "normal"))
    goto( x1, y1)       # have to go back because the write functions move the turtle
    down()              # now to start drawing the line

    # plot second set of coords
    goto( x2, y2)
    up()
    dot( size=4)
    write( "Angle R: ", True, font=("Arial", 12, "normal"))
    write( round(angle_c * 100) / 100.0, True, font=("Arial", 12, "normal"))
    write( deg, True, font=("Arial", 12, "normal"))
    goto( x2 ,y2)       # have to go back because the write functions move the turtle
    down()

    # plot last set of coords
    goto( x3, y3)
    dot( size=4)
    write( "Angle P: ", True, font=("Arial", 12, "normal"))
    write( round(angle_a * 100) / 100.0, True, font=("Arial", 12, "normal"))
    write( deg, True, font=("Arial", 12, "normal"))
    goto( x3, y3)       # have to go back because the write functions move the turtle
    down()

    goto( x1, y1)       # have to end where we started or only 2 sides will be drawn

    
# Write a string s at the specified location (x, y)
def text( s, x, y):
    penup() # Pull the pen up
    goto( x, y)
    pendown() # Pull the pen down
    write(s) # Write a string
    
# Draw a point at the specified location (x, y)
def draw_point(x, y):
    penup() # Pull the pen up
    goto( x, y)
    pendown() # Pull the pen down
    begin_fill() # Begin to fill color in a shape
    circle( 3)
    end_fill() # Fill the shape

# Draw a circle centered at (x, y) with the specified radius
def circles( x=0, y=0, radius=10, step=1):
    penup() # Pull the pen up
    goto(x, y - radius)
    pendown() # Pull the pen down
    circle( radius, extent=None, steps=step)
    
# Draw a rectangle at (x, y) with the specified width and height
def rectangle( x=0, y=0, width=10, height=10):
    penup() # Pull the pen up
    goto( x + width / 2, y + height / 2)
    pendown() # Pull the pen down
    right( 90)
    forward( height)
    right( 90)
    forward( width)
    right( 90)
    forward( height)
    right( 90)
    forward( width)