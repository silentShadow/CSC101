'''\
Rev: 1
Name: silentshadow
Description: 
Reference: exercise 6.3
Page: 203 (PDF 223)
'''



def palindrome( n):
    if ( n[ ::-1] ) == n :
        print( "Found one!")
    else:
        print( "Sorry")

    
    
def main():
    print( "Let's find us a Palindrome number!")
    n = input( "Give a number:  ")
    palindrome( n)
    
    

if __name__ == '__main__': main()