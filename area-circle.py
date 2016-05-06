import turtle as t
from math import pow, pi


def compute_area(radius):
    """\
    This is the function for computing the
    area of a circle
    """
    radius = int(input("What is the radius of the circle? \n> "))
    
    while radius <=0:
        radius = int(input("Sorry, must give a number greater than 0. \n> "))
    
    area = (pi * pow(radius, 2))
    
    #t.circle(radius)
        
    return area
    


def main():
    """This is the main function"""
    a = compute_area(20)
    #t.done()
    print(a)
    
    
if __name__ == "__main__" : main()