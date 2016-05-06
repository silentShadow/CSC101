# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 08:56:23 2016

@author: jonman
@description: draws a spiral with a radius not exceeding 
    the orginal x,y coords
"""

import turtle as t


def draw_spiral(radius):
    original_xcor = t.xcor()
    original_ycor = t.ycor()
    speed = 1
    while True:
        t.forward(speed)
        t.left(10)
        speed += 0.1
        if t.distance(original_xcor, original_ycor) > radius:
            break

    
        
def main():
    draw_spiral(100)
    t.exitonclick()
        
if __name__ == "__main__" : main()