'''\
Rev: 1
Author: SilentShadow
Description: displaying dates and times
Reference: Listing 2.8
Page: 51 (PDF 71)
Formula: monthly payment = loanAmt * monthlyAPR / ( 1 - 1/(1 + monthlyAPR)**(years*12) )
         total payment = monthly payment * years * 12
'''



# Grab user data
def loans():
    apr = float(input( "Enter your APR, e.g., 3.25 \n" ))
    monthly_apr = apr / 1200
    
    years = int(input( "Enter number of years for the loan \n" ))
    loan_amt = float(input( "Enter the amount of the loan \n" ))
    
    monthly_payment = loan_amt * monthly_apr / ( 1 - 1/(1 + monthly_apr) ** (years * 12) )
    total_payment = monthly_payment * years * 12
    
    print( "Monthly payment is {}".format( int(monthly_payment * 100)/100 ) )
    print( "Total payment is {}".format( int(total_payment * 100)/100 ) )
    

def main():
    loans()
    

if __name__ == "__main__" : main()