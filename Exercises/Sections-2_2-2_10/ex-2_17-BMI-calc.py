'''\
Rev: 1
Name: silentshadow
Description: calculates BMI based on user supplied weight and height
Reference: exercise 2.17
Page: 59 (PDF 79)
'''


def calc_bmi():
    pounds = float( input( "Enter your weight (lbs):  >"))
    inches = int( input( "Enter your height (in):  >"))
    BMI = (pounds / ( inches * inches )) * 703

    print( "Based on a weight of {} lbs and height of {} inches, your BMI is {:.2f}".format( pounds, inches, BMI))
    
    
def main():
    calc_bmi()
    

if __name__ == "__main__" : main()