'''\
Rev: 1
Name: silentshadow
Description: returns the hex value of a passed decimal number
Reference: listing 6.8
Page: 186 (PDF 206)
'''

def decToHex(dec_val):
    hex = " "
    while dec_val != 0:
        hex_val = dec_val % 16
        hex += toHexChar( hex_val)
        dec_val = dec_val // 16
    return hex


def toHexChar(hex_val):
    if 0 <= hex_val <= 9:
        return chr( hex_val + ord( '0'))
    else:
        return chr( hex_val - 10 + ord( 'A'))


def main():
    dec_val = eval( input( "Enter decimal number, e.g. 255:  "))
    print( "{} to HEX is{}".format( dec_val, decToHex( dec_val)))


if __name__ == '__main__': main()