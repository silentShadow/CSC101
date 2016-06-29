'''\
Rev: 1
Name: silentshadow
Description: pentagonal numbers:  n( 3n - 1) / 2 for n = 1, 2, etc
Reference: ex 6.1
Page: 203 (PDF 223)
'''

def get_pentagonal_number( n):
    '''This function finds the pentagonal number for n'''
    for i in range( n):
        print( ((i * ( 3 * i - 1)) / 2), end=', ' )
    print()
    #return (n * ( 3 * n - 1)) / 2
    
    
def main():
    p = get_pentagonal_number( 10)
    #print( p)
    
if __name__ == "__main__" : main()