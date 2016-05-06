def greet( name):
    print( "Hello, {}".format( str(name)))
    
    return None
    
    
def report(hr, wg, gross):
    print( "{:-^19}".format( "Summary"))
    print( "Hours: {}".format( hr))
    print( "Wages: ${:.2f}".format( wg))
    print( "Gross: ${:.2f}".format( gross))
    
    return None
    
    
def addition(hours, wages):
    gross_pay = hours * wages
    
    report( hours, wages, gross_pay)
    
    
    
def main():
    greet('Jonny Bravo')
    
    addition(40, 10.75)
    
    
if __name__ == "__main__" : main()