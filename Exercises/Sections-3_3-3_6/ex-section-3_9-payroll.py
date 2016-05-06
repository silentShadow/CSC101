'''\
Rev: 1
Name: silentshadow
Description: 
Reference: exercise 3.9
Page: 87 (PDF 107)
'''


def report(name, hours, wages, fed, fed_hold, state, state_hold, gross, net):
    '''\
    This is the final report function
    '''
    
    print( "\n{:-^30}".format( "Weekly Summary"))
    print( "Hours worked: {}".format( hours))
    print( "Hourly wage: ${}".format( wages))
    print( "Gross pay: ${}".format( gross))
    print( "\n{:-^30}".format( "Deductions"))
    print( "Federal withholding ({:.1%}): ${:.2f}".format( fed, fed_hold))
    print( "State withholding ({:.1%}): ${:.2f}".format( state, state_hold))
    print( "\n{:-^30}".format( "Adjusted wages"))
    print( "Net Pay: ${:.2f}".format( net))
    print()


def payroll_info():
    '''\
    This functions grabs the user information
    '''
    
    e_name    = str( input( "enter employee's name:  >"))
    hours     = int( input( "enter hours worked this week:  >"))
    wage      = float( input ( "enter hourly wage:  >"))
    fed_tax   = float( input( "enter federal tax withholding:  >"))
    state_tax = float( input( "enter state tax withholding:  >"))
    
    gross_pay  = hours * wage
    fed_hold   = gross_pay * fed_tax
    state_hold = gross_pay * state_tax
    net_pay    = gross_pay - fed_hold - state_hold 
    
    report(e_name, hours, wage, fed_tax, fed_hold, state_tax, state_hold, gross_pay, net_pay)
    
    
def main():
    '''\
    This is the main function
    '''
    
    payroll_info()
    
    
    
    
if __name__ == "__main__" : main()