'''\
Rev: 1
Name: silentshadow
Description:
Reference: exercise 2.5
Page: 56 (PDF 76)
'''

def tip():
    check_total = float(input( "What was the amount of the check?  >" ))
    tip_amt =  float(input( "How much would you like to tip, e.g. 10% ,15%  >" ))
    
    tip_total = (check_total * tip_amt/100)
    grand_total = check_total + tip_total
    
    print( "Gratuity will be ${:.2f} totaling ${:.2f}".format( tip_total, grand_total ) )
    
    
def main():
    t = tip()
    
    
if __name__ == "__main__" : main()