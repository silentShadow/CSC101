'''\
Rev: 1
Name: silentshadow
Description: returns the gcd of 2 numbers
Reference: listing 6.5
Page: 183 (PDF 203)
'''


def gcd( n1, n2):
    gcd = 1
    k = 2
    
    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k
        k += 1
            
    return gcd


