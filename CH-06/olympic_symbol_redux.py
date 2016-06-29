'''\
Class: CSC101 Week 6
Rev: 1
Name: silentshadow
Description: this program will utilize functions to draw the olympic rings
Reference: week 6 assignemnt A
'''

from turtle import *

setup(500, 500)                     # make window set size
win = Screen()                      # refer to the screen as win
win.title( "Olympic Rings!")        # change the window title



def drawRing(x, y, radius = 10, width = 2, color = "black"):
    penup()
    goto( x, y)
    pensize( width)
    pencolor( color)
    pendown()
    circle( radius)



def main():
    hideturtle()
    drawRing( -110, -25, 45, color = "blue")
    drawRing( 0, -25, 45)
    drawRing( 110, -25, 45, color = "red")
    drawRing( -55, -75, 45, color = "yellow")
    drawRing( 55, -75, 45, color = "green")
    done()



if __name__ == '__main__': main()