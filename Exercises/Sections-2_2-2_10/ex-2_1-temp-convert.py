'''\
Rev: 1
Name: silentshadow
Description:
Reference: exercise 2.1
Page: 55 (PDF 75)
'''


def convert():
    cel = float(input( "Give a degree in Celsius:  " ))
    fahr = (9/5) * cel + 32
    
    return fahr
    

def main():
    temp = convert()
    print( temp )
    
    
if __name__ == "__main__" : main()