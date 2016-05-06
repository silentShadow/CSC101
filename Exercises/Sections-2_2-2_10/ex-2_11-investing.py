'''\
Rev: 1
Name: silentshadow
Description: returns amount needed to invest to return a $5,000 ROI 
Reference: exercise 2.11
Page: 58 (PDF 78)
'''

from math import pow


def invest():
    wanted_value = int( input( "How much do you want your account to be worth?  >"))
    APR = float( input( "What is the APR?  >"))
    years = int( input( "How many years?  >"))
    deposit = (wanted_value) / pow( (1 + (APR /12)), (years /12))
    
    print( "In order to gain a value of ${} at an interest rate of {}%, you must deposit ${:.2f}".format(wanted_value,APR,deposit))
    
    
def main():
    i = invest()
    
    
if __name__ == "__main__" : main()