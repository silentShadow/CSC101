'''\
revision: 1
author: jonathan reiter
description: turtle program drawing my initials
reference: pages 21 - 24
'''

from turtle import *


hideturtle()                                    # Don't want to see the turtle
up()                                            # Pen up

pen( pensize=3, pencolor='green')
down()


# Draw the 'J'
left( 90)
forward( 80)
home()
right( 90)
circle( -25, 180)  
up()                             


# Draw and fill the square
color( 'orange', 'black')
setheading( 90)
begin_fill()
goto( 67, -40)
down()
goto( 67, 95)
left( 90)
forward( 56)
left( 90)
forward( 135)
goto( 67, -40)
end_fill()


# Draw the 'R'
up()
setheading( 90)
color( 'yellow')
goto(20, -25)
down()
forward( 105)
right( 90)
circle( -32, 180)
left( 140)
goto( 60, -25)
up()

done()                                          # Admire the masterpiece
