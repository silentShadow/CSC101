'''\
Rev: 1
Name: silentshadow
Description: ascii codes and their equivalent
Reference: listing 3.3.3
Page: 69 (PDF 79)
'''
print()

upper = []
lower = []
ascii = []

for i in range(97,123):
    lower.append( chr( i))
    #print( "{} is {}".format(i, chr( i)), sep=' ', end='\n')

for i in lower:
    ascii.append( ord( i))
    #print( "{} is {}".format( i, ord( i)), sep=' ', end='\n')
    
for i in lower:
    upper.append( chr( ord( i) - 32))
    #print( "Capital of {} is {}".format( i, chr( ord( i) - 32 )))
    
print()
print( lower)
print()
print( ascii)
print()
print( upper)
print()
