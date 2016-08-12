from circle import Circle
from rectangle import Rectangle
from random import randint


############
## COLORS ##
############
BLK = '\033[1;30m'
RED = '\033[1;31m'
GRN = '\033[1;32m'
YLW = '\033[1;33m'
BLU = '\033[1;34m'
MAG = '\033[1;35m'
CYN = '\033[1;36m'
NC = '\033[0m'


def create_random_shapes(shapesList):
    """Creates 5 rand circs and 4 rand rects"""
    for _ in range(5):
        shapesList.append( Circle(randint(1,5)) )

    for _ in range(5):
        shapesList.append( Rectangle(randint(1,5), randint(1,5)) )



def print_list(shapesList):
    """Print the list"""
    c=1
    r=1
    for obj in shapesList:
        if isinstance(obj, Circle):
            print("{0}Circle object {1} {2}".format(RED, c, NC))
            print('\t',obj.__str__())
            c += 1
        else:
            print("{0}Rectangle object {1} {2}".format(CYN, r, NC))
            print('\t', obj.__str__())
            r += 1
    return [item for item in shapesList]



def double_dimensions(shapesList):
    """Doubles the dimensions from the list"""
    for obj in shapesList:
        if isinstance(obj, Circle):
            #print("Current radius is: {}".format(obj.getRadius()))
            #print("\tDoubling value...")
            obj.setRadius(obj.getRadius() * 2)
        else:
            #print("Current Width: {} and Height: {}".format(obj.getWidth(), obj.getHeight()))
            #print("\tDoubling values...")
            obj.setHeight(obj.getHeight() * 2)
            obj.setWidth(obj.getWidth() * 2)



def main():
    """Main function here"""
    print("Creating random Circles and Rectangles...")
    shapes = []
    create_random_shapes(shapes)

    print("These are the shapes created:")
    print_list(shapes)

    print("Doubling the dimensions of the shapes...")
    double_dimensions(shapes)

    print("Shapes after doubling dimensions:")
    print_list(shapes)



main()