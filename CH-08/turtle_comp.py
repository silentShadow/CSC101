'''
rev: 1
class: CSC101 week 7 program b
description: draws a picture following a sequence of instructions submitted by user
author: jonathan reiter

'''

import turtle as t

# Setup
t.setup(1000, 1000)                   # make window set size
win = t.Screen()                    # refer to the screen as win
win.title( "Turtle Computer!")      # change the window title
win.bgcolor( "black")               # change background color
t.pencolor("green")

# constants
KEY = "fblrud"


def get_command():
    repeater = ''
    cmd = ''
    usr_cmd = input( "Enter your program:  ")
    turn_angle = input( "Set turn angle in ° (degrees):  ")
    mov_length = input( "Set length of movement:  ")

    # there has to be a better way!! 
    for index in range( 0, len( usr_cmd) - 1):
        if usr_cmd[ index].isdigit() and usr_cmd[ index + 1] in KEY:
            if usr_cmd[ index + 1] == 'f':
                up( mov_length, usr_cmd[ index])
            elif usr_cmd[ index + 1] == 'b':
                down( mov_length, usr_cmd[ index])
            elif usr_cmd[ index + 1] == 'l':
                left( turn_angle, usr_cmd[ index])
            elif usr_cmd[ index + 1] == 'r':
                right( turn_angle, usr_cmd[ index])
            else:
                break
        elif usr_cmd[ index] in KEY:
            if usr_cmd[ index] == 'f':
                up( mov_length)
            elif usr_cmd[ index] == 'b':
                down( mov_length)
            elif usr_cmd[ index] == 'u':
                penup()
            elif usr_cmd[ index] == 'd':
                pendown()
            elif usr_cmd[ index] == 'l':
                left( turn_angle)
            else:
                right( turn_angle)
        else:
            print( "You broke it")
    
    



def up( dist, times=1):
    #setheading(90)
    repeat = int( times)
    while repeat > 0:
        t.forward( int( dist))
        repeat -= 1


def down( dist, times=1):
    #setheading(270)
    repeat = int( times)
    while repeat > 0:
        t.backward( int( dist))
        repeat -= 1


def left( angle, times=1):
    #setheading(180)
    repeat = int( times)
    while repeat > 0:
        t.left( int( angle))
        repeat -= 1


def right( angle, times=1):
    #setheading(0)
    repeat = int( times)
    while repeat > 0:
        t.right( int( angle))
        repeat -= 1


def penup():
    t.up()


def pendown():
    t.down()


def pos( x, y):
    t.write( t.position(), font=('Arial',12,'normal'))
    print( t.position())


def inititals():
    t.up()
    t.color('green')
    t.goto(500, -420)
    # Draw the 'J'
    t.setheading( 90)
    t.down()
    t.forward( 80)
    t.up()
    t.down()
    t.goto(500, -420)
    t.right( 180)
    t.circle( -25, 180)  
    t.up()                             


    # Draw and fill the square
    #t.color( 'orange', 'black')
    #t.setheading( 90)
    #t.begin_fill()
    #t.goto( 567, -540)
    #t.down()
    #t.goto( 567, -595)
    #t.left( 90)
    #t.forward( 56)
    #t.left( 90)
    #t.forward( 135)
    #t.goto( 567, -540)
    #t.end_fill()


    # Draw the 'R'
    t.up()
    t.setheading( 90)
    t.color( 'yellow')
    t.goto( 520, -525)
    t.down()
    t.forward( 105)
    t.right( 90)
    t.circle( -32, 180)
    t.left( 140)
    t.goto( 560, -525)
    t.up()


def main():
    program_key = '''
*** Welcome to Computer Turtle ***

Character       Meaning
f...............move turtle forwad
b...............move turtle backward
l...............turn turtle left
r...............turn turtle right
u...............pen up
d...............pen down

'''
    print( program_key)
    print( "Right click the turtle for more info...")
    get_command()
    t.listen()
    t.onclick( pos, 2)
    inititals()

    t.mainloop()
    



if __name__ == '__main__': main()