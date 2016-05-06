'''\
Rev: 1
Name: silentshadow
Description: computing the compound interest
Reference: exercise 2.21
Page: 60 (PDF 80)
'''

def calc_interest(principal, rate, months):
    '''\
    This is the compound interest function
    principal * (1 + rate)^periods = new value
    '''
    #pr = 1 + rate
    #principal *= pow(pr, months)
    
    for i in range(0,months):
        principal = (1 + rate) * principal
        
    print( "After {} months, the new value is ${:.2f}".format( months, principal))
    
    
 


def main():
    p = int( input( "Enter the monthly savings amount:  >"))
    r = float( input( "Enter the APR e.g. .05:  >"))
    m = int( input( "Enter number of months:  >"))
    c = calc_interest(p, r, m)
    
    
    
if __name__ == "__main__" : main()