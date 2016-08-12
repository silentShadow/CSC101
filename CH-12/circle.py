from geo_objects import GeometricObject
import math


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


class Circle(GeometricObject):
    """The circle class"""

    def __init__(self, radius):
        """"""
        super().__init__()
        self.__radius = radius

    def getRadius(self):
        """"""
        return self.__radius

    def setRadius(self, radius):
        """"""
        self.__radius = radius

    def getArea(self):
        """"""
        return self.__radius * self.__radius * math.pi

    def getDiameter(self):
        """"""
        return 2 * self.__radius

    def getPerimeter(self):
        """"""
        return 2 * self.__radius * math.pi

    def printCircle(self):
        """"""
        print(self.__str__() + " radius: " + str(self.__radius))

    def __str__(self):
        """"""
        return "{0}radius: {1}{2}{3}".format(YLW, MAG, str(self.__radius), NC)