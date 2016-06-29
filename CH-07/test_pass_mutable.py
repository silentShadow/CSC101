'''\
rev: 1
author: jonathan reiter
description: 
reference: listing 7.5
page: 225 (PDF 245)
'''

from circle_class import Circle


def print_areas(c, times):
    print( "{}{:.>20}".format( "Radius", "Area"))
    while times >= 1:
        print( "{}{:.>25.2f}".format( c.radius, c.get_area()))
        c.radius += 1
        times -= 1


def main():
    c1 = Circle()
    n = 5

    print_areas( c1, n)
    print()
    print( "Radius {:.>19}".format( c1.radius))
    print( "n {:.>24}".format( n))


if __name__ == '__main__': main()