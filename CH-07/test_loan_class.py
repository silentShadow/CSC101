from loan_class import Loan

def main():
    # Enter yearly interest rate
    APR = eval( input( "Enter yearly interest rate, for example, 7.25: "))
    # Enter number of years
    years = eval( input( "Enter number of years as an integer: "))

    # Enter loan amount
    amount = eval( input( "Enter loan amount, for example, 120000.95: "))

    # Enter a borrower
    borrower = input( "Enter a borrower's name: ")

    # Create a Loan object
    loan = Loan( APR, years, amount, borrower)


    # Display loan date, monthly payment, and total payment
    print("The loan is for {}".format( loan.get_borrower()) )
    print("The monthly payment is ${:.2f}".format( loan.get_monthly_payment()) )
    print("The total payment is ${:.2f}".format( loan.get_total_payment()) )



if __name__ == '__main__': main()