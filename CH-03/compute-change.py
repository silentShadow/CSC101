'''\
Rev: 1
Name: silentshadow
Description: computing the amount of change due
Reference: listing 3.4
Page: 73 (PDF 83)
'''

amt = float( input( "Enter a dollar amount:  >"))
amt_left = int( amt *100)

singles = amt_left // 100
amt_left %= 100

quarters = amt_left // 25
amt_left %= 25

dimes = amt_left // 10
amt_left %= 10

nickels = amt_left // 5
amt_left %= 5

pennies = amt_left

print( "The amount {} has {} dollar(s), {} quarter(s), {} dime(s), {} nickel(s), and {} pennies".format( amt, singles, quarters, dimes, nickels, pennies))
 