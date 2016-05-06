# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 09:16:31 2016

@author: jonman
"""
#
#a a^2 a^3
#1 1 1
#2 4 8
#3 9 27
#4 16 64

print("{:<10}{:<10}{}".format("a","a^2","a^3"))
for num in range(1,5):
    print("{:<9d} {:<9d} {:d}".format(num,num*num,num*num*num))