'''\
Rev: 1
Author: silentshadow
Description: learning how to use the functools and operator modules
Reference: https://docs.python.org/3/howto/functional.html
'''

import functools, operator

nums = [1,2,3,4,5,6,7,8,9]

sums = functools.reduce(operator.add, nums, 0) # Should yield 45
print( "Using the functools.reduce(operator.add, nums, 0) to sum the ints in a list")
print( sums)

