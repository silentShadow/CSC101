# -*- coding: utf-8 -*-
"""\
Rev: 2
Author: silentshadow
Description: sum the ints in a list
Reference: Section: 1.6, 1.6
"""

# Opt 1:
nums = [1,2,3,4,5,6,7,8,9]
print(sum(nums))  # Should yied 45

# Opt 2:
sums = functools.reduce(operator.add, nums, 0) # Should yield 45
print( sums)