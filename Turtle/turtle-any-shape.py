"""\
Rev: 1
Author: silentshadow
Description: draw any shape based on the number of sides and the length of each

"""
import turtle as t


# Draw any shape given # of sides
#   and desired length
def draw_shape(sides, length):
    for _ in range(sides):
        t.forward(length)
        t.right(360 / sides)


def hexagon(size):
    for _ in range(6):
        t.forward(size)
        t.left(60)


def line_without_moving(length):
    t.forward(length)
    t.backward(length)
    

def star_arm():
    line_without_moving(50)
    t.right(360 / 5)
    

def main():
#    for i in range(5):
#        star_arm()
#    hexagon(50)
    side = int( input( "Enter the sides:  >"))
    leng = int( input( "Enter the length of each side:  >"))
    draw_shape( side, leng)
    
    t.exitonclick()
    
if __name__ == "__main__" : main()