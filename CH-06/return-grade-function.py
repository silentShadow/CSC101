'''\
Rev: 2
Name: silentshadow
Description: returns the letter grade for percentile score
Reference: listing 6.3
Page: 177 (PDF 197)
'''

import sys


def grade( score):
    if score < 0 or score > 100:
        print( "Not a valid score")
        return

    if score >= 90.0:
        return "A"
    elif score >= 80.0:
        return "B"
    elif score >= 70.0:
        return "C"
    elif score >= 60.0:
        return "D"
    else:
        return "F"
             
        
def main():
    score = float( input( "Enter score, e.g. 92.3:  "))
    print( "Grade is {}".format( grade( score)))


if __name__ == '__main__':
    sys.exit(int(main() or 0))