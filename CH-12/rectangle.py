from geo_objects import GeometricObject


############
## COLORS ##
############
BLK = '\033[30m'
RED = '\033[31m'
GRN = '\033[32m'
YLW = '\033[33m'
BLU = '\033[34m'
MAG = '\033[35m'
CYN = '\033[36m'
NC = '\033[0m'


class Rectangle(GeometricObject):
    """"""
    def __init__(self, width = 1, height = 1):
        """"""
        super().__init__()
        self.__width = width
        self.__height = height

    def getWidth(self):
        """"""
        return self.__width

    def setWidth(self, width):
        """"""
        self.__width = width

    def getHeight(self):
        """"""
        return self.__height

    def setHeight(self, height):
        """"""
        self.__height = height

    def getArea(self):
        """"""
        return self.__width * self.__height

    def getPerimeter(self):
        """"""
        return 2 * (self.__width + self.__height)
    
    def print_rectangle(self):
        """"""
        print(self.__str__() + " width: " + str(self.__width) + " height: " + str(self.__height))
    
    def __str__(self):
        """"""
        return "{0}width: {1}{2}{3} height: {4}{5}{6}".format( YLW, MAG, str(self.__width), YLW, MAG, str(self.__height), NC)
