from math import pi,pow

radius = eval(input("Give a radius: \n> "))
# exec(compile("import os;print(os.name)",'test','exec'))
# __import__("os").unlink("importantsystemfile")

area = pi * pow(radius, 2)

print("Area of the circle is: {}".format(area))

