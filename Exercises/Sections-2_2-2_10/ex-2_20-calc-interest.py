'''\
Rev: 1
Name: silentshadow
Description: computing the interest on the nect monthly payment
Reference: exercise 2.20
Page: 60 (PDF 80)
'''

def calc_interest():
    bal = int( input( "Enter a balance:  >"))
    APR = float( input( "Enter the APR:  >"))
    interest = bal * (APR / 1200)

    print( "The interest is {:.2f}%".format( interest))


def main():
    calc_interest()
    
    
if __name__ == "__main__" : main()