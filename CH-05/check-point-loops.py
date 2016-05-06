print( "{:-^40}".format( ''))
i=0
while i<5:
    print( "i is:",i)
    for j in range( i, 1, -1):
        print( 'j is:',j, end=' ')
    print( '****')
    i+=1
    

print( "{:-^40}".format( ''))
a=5
while a >= 1:
    print( 'a is:',a)
    num=1
    for b in range( 1, a+1):
        print( 'b is:',b)
        print( num, end='xxx')
        num *= 2
    print()
    a -= 1
    
print( "{:-^40}".format( ''))
c=5
while c >= 1:
    num = 1
    for j in range( 1, c + 1):
        print( num, end='xxx')
        num *= 2
    print()
    c -= 1
    
print( "{:-^40}".format( ''))
d=1
while d <= 5:
    num = 1
    for j in range( 1, d + 1):
        print( num, end='G')
        num += 2
    print()
    d += 1

print()