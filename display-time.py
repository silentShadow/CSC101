'''\
Rev: 1
Author: SilentShadow
Date: 20 APR 16
Description:
Reference: Listing 2.5
Page: 41
'''

# Get user input
secs = int( input("Give a number for seconds \n") )

# Grab remaining time
mins = secs // 60
secsRemain = secs % 60

print( "{} seconds is {} minutes and {} seconds".format( secs, mins, secsRemain ) )
