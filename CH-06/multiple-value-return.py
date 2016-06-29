'''\
Rev: 1
Name: silentshadow
Description: return several values from a function
Reference: listing 6.10
Page: 190 (PDF 210)
'''

def sorts( n1, n2):
    if n1 < n2:
        return n1, n2
    else:
        return n2, n1
        
        
num1, num2 = sorts( 3, 2)
print( "n1 is {} and n2 is {}".format( num1, num2))
