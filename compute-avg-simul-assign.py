'''\
Rev: 1
Author: silentShadow <ReiterJ@protonmail.com>
Description: silmultaneous assignments to comptue averages
'''

num1, num2, num3 = eval(input("Give three ints comma delimited \n"))

avg = ( num1 + num2 + num3 ) / 3

print( "Average of {} {} {} is {}".format( num1,num2,num3,avg ) )