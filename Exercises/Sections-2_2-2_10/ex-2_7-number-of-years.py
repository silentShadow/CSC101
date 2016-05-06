'''\
Rev: 1
Name: silentshadow
Description: find the number of years and days given the number of minutes
Reference: exercise 2.7
Page: 56 (PDF 76)
'''

def find_days(mins):
    # Find number of days from given minutes
    days = mins // 60 // 24
    
    # Find number of years from given minutes
    years = mins // 365 // 60 // 24
    
    print( "Approximately {} year(s) and {} day(s)".format(years, days) )
    return years, days
    
    
def main():
    m = int(input( "Give the number of minutes  >" ))
    d = find_days( m )
    
    
if __name__ == "__main__" : main()