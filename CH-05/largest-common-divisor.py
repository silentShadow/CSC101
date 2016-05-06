'''\
Rev: 1
Name: silentshadow
Description: 
Reference: listing 5.8
Page: 148 (PDF 168)
'''

n1 = int( input( "First num  >"))
n2 = int( input( "Second num  >"))
gcd = 1
k = 2

while k <= n1 and k <= n2:
    if n1 % k == 0 and n2 % k == 0:
        gcd = k
    k += 1
    
print( "GCD for {} and {} is {}".format( n1, n2, gcd))