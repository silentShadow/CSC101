'''\
Rev: 1
Name: silentshadow
Description: splits a four digit number and displays the result in reverse order
Reference: exercise 2.13
Page: 58 (PDF 78)
'''

num = input( "Enter a four digit number:  >")

# Opt 1: The hard way
ones  = int( int( num) %10)
tens  = int( int( num) /10 %10)
hunds = int( int( num) /100 %10)
thous = int( int( num) /1000)

print( "This is the hard way...")
print( thous, hunds, tens, ones, sep='\n', end='\n\n')


#Opt 2: Easy way
print( "This is the easy way... using a for loop over the user passed value")
for i in num:
    print( i)