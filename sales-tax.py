'''\
Rev: 1
Author: SilentShadow
Description: computes sales tax
Reference: Listing 2.6
Page: 46 (PDF 66)
'''

cashAmount = float( input( "What was the cash value? \n" ) )

tax = cashAmount * .06

print( "Sales tax is {}".format( (tax * 100) / 100 ) )