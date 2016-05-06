# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 10:12:57 2016

@author: jonman
@decription: dictionaries
"""

capitals = {'United States':'Washington DC','France':'Paris','Italy':'Rome'}

print(capitals.keys())
print(capitals.values())
print()

for i in capitals:
    print("That capital of {} is {}".format(i,capitals[i]))

print()

for key, value in capitals.items():
    print(key, value)
    
    