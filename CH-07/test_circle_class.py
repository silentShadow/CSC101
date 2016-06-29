'''\
rev: 1
author: jonathan reiter
description: 
reference: listing 7.2
page: 221 (PDF 240)
'''

from circle_class import Circle


def main():
    print( "Variable {:>23}".format( "Value"))

    c1 = Circle()
    print( "area c5 {:.>24.2f}".format( c1.get_area()))

    c25 = Circle( 25)
    print( "area c25 {:.>23.2f}".format( c25.get_area()))


if __name__ == '__main__': main()