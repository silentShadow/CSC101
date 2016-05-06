'''\
Rev: 2
Name: silentshadow
Description: sum the digits in an integer
Reference: exercise 2.6
Page: 56 (PDF 76)
'''


def digit_sum(num):
    # Opt 1: keep input as a string and use map 
    #sums = sum(map(int,str(num)))
    #print( "Everything as strs {}".format(sums) )
    
    # Opt 2:
    print( sum(num) )
        
    # Opt 3:
    ones  = int( int( num) % 10)
    tens  = int( int( num)/ 10 % 10)
    hunds = int( int( num)/ 100)
    sums = ones + tens + hunds
    
    print( "The sum of the digits in {} is {}".format(num, sums) )


def main():
    nums = str(input( "Give a number between 0 and 1000  >" ))
    
    # Opt 1; comment this out to run Opt 2 or 3
    #d = digit_sum(nums)
    
    # Opt 2; comment this out to run Opt 1 or 3
    [ digit_sum(num) for num in [ map(int,str(nums)) ] ]
    
    
    
    
if __name__ == "__main__": main()