'''\
Rev: 1
Name: silentshadow
Description: 
Reference: listing 5.6
Page: 145 (PDF 165)
'''

print( "{:^40}".format( "Multiplication Table"))

print( "   ", end='')

for x in range( 1, 10):
    print( "  ", x, end='')

print()
print("{:-^40}".format( '-'))

for i in range( 1, 10):
    print( i, '|', end='')
    for y in range( 1, 10):
        print( "{:4d}".format( (i*y)), end='')
    print()