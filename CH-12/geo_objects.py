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


class GeometricObject:
    """"""
    def __init__(self, color = "green", filled = True):
        """"""
        self.__color = color
        self.__filled = filled

    def getColor(self):
        """"""
        return self.__color

    def setColor(self, color):
        """"""
        self.__color = color

    def isFilled(self):
        """"""
        return self.__filled

    def setFilled(self, filled):
        """"""
        self.__filled = filled

    def __str__(self):
        """The string"""
        return "color: " + self.__color + " and filled: " + str(self.__filled)

