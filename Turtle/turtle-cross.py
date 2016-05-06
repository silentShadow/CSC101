# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 08:32:09 2016

@author: jonman
@description: drawing a cross
@ref: Section: 1.9, 
"""

import turtle as t


def line_without_moving():
    t.forward(50)
    t.backward(50)
    
    
def main():
    for i in range(4):
        line_without_moving()
        t.right(90)
    t.exitonclick()
    

if __name__ == "__main__": main()