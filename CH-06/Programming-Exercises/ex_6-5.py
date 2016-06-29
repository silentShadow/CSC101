'''\
Rev: 1
Name: silentshadow
Description: 
Reference: exercise 6.5
Page: 203 (PDF 223)
'''

def show_sorted( ):
    u = ' '
    s = []
    while True:
        u = input( "Enter a number, 'q' to quit:  ")
        if u.lower() != 'q':
            s.append( int( u))
        else:
            break

    #print( s)
    print( sorted( s))
    
    
def main():
    show_sorted()



if __name__ == '__main__': main()