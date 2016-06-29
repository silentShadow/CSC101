'''\
Rev: 1
Name: silentshadow
Description: import the rand_char module and print 175 'random' chars
Reference: listing 6.12
Page: 192 (PDF 213)
'''

from rand_char import *


n_chars = 175
ch_line = 25


for _ in range( n_chars):
    print( rand_lower(), end='')
    if (_ + 1) % ch_line == 0:
        print()
 