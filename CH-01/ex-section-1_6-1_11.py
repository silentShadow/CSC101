# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 13:14:30 2016

@author: jonman
@ref: Section: 1.6, 1.11
"""

birth = 7
death = 13
immig = 45
year  = 365
secs  = 60
mins  = 60
days  = 24

popul = 3120342486

day_seconds  = secs * mins * days
year_seconds = day_seconds * year
year_births  = year_seconds // birth
year_deaths  = year_seconds // death
year_immig   = year_seconds // immig

one_year_pop  = year_births - year_deaths + year_immig
first_yr_pop  = popul + one_year_pop
second_yr_pop = first_yr_pop + one_year_pop
third_yr_pop  = second_yr_pop + one_year_pop
fourth_yr_pop = third_yr_pop + one_year_pop
fifth_yr_pop  = fourth_yr_pop + one_year_pop



#print(day_seconds)
#print(year_seconds)
#print(year_births)
#print(year_deaths)
#print(year_immig)
print(one_year_pop, end='\n\n')
print(first_yr_pop, end='\n\n')
print(second_yr_pop, end='\n\n')
print(third_yr_pop, end='\n\n')
print(fourth_yr_pop, end='\n\n')
print(fifth_yr_pop, end='\n\n')