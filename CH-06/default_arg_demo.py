'''\
Rev: 1
Name: silentshadow
Description: defining functions with default args
Reference: listing 6.9
Page: 189 (PDF 209)
'''


def print_area(w=1, h=2):
    area = w * h
    print( "width: {}, height: {}, area: {}".format( w, h, area))
    
    
print_area()
print_area(4, 2.5)
print_area(h=5, w=3)
print_area(w=1.2)
print_area(h=6.2)
