'''\
Rev: 1
Name: silentshadow
Description: returns the gcd of 2 numbers
Reference: listing 6.5
Page: 183 (PDF 203)
'''

import sys


def is_prime( n):
    divisor = 2
    while divisor <= n / 2:
        if n % divisor == 0:
            return False  # Not a prime number
        divisor += 1
            
    return True       # Is prime


def print_prime( n_primes):
    primes          = 50
    primes_per_line = 10
    count           = 0
    number          = 2
    
    while count < primes:
        if is_prime( number):
            count += 1
            print( number, end=' ')
            
            if count % primes_per_line == 0:
                print()
                
        number += 1
        


def main():
    p = print_prime( 50)
    print( "1st 50 primes are: {}".format( p))


if __name__ == '__main__':
    sys.exit(int(main() or 0))