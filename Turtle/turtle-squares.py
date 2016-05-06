# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 07:59:19 2016

@author: jonman
@description: drawing 4 squares
@ref: Section: 1.9, 1.12
"""


import turtle as t


def squares():
    """\
    Draw the exterior border
    """
    for i in range(3):
        t.left(20)
        for i in range(4):
            t.forward(100)
            t.left(90)
    t.exitonclick()
    
#    t.up()
#    t.forward(50)
#    t.down()
#    t.left(90)    
#    t.forward(100)
#    t.up()
#    t.backward(50)
#    t.left(90)
#    t.down()
#    t.forward(50)
#    t.backward(100)

#    t.done()
    
    
def main():
    squares()
    
    
if __name__ == "__main__": main()