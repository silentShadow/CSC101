'''\
Rev: 1
Name: silentshadow
Description: prints the letter grade for percentile score
Reference: listing 6.2
Page: 176 (PDF 196)
'''

import sys


def grade( score):

    if score >= 90.0:
        print( "A")
    elif score >= 80.0:
        print( "B")
    elif score >= 70.0:
        print( "C")
    elif score >= 60.0:
        print( "D")
    else:
        print( "F")
             
        
def main():
    score = float( input( "Enter score, e.g. 92.3:  "))
    print( "Grade is {}".format( grade( score)))


if __name__ == '__main__':
    sys.exit(int(main() or 0))