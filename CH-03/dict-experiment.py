d = {}.fromkeys( ['x1','x2','x3','y1','y2','y3'],0)
print( d)

for k in list( sorted( d.keys())):
    d[ k] = float( input( "Give a value for {}:  >".format( k)))
    print( k, d[ k])
    
print( d)

