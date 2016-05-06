#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#
# Description:  fun with dictionaries
# Reference: Lynda.com 5.6: dictionaries
# dictionaries.py


def main():

    # Create a dictionary with five items
    d = dict(
        one=1, two=2, three=3, four="four", five="five"
    )
    d['seven'] = 7

    for i in sorted(d.keys()):
        print(i,d[i])

if __name__ == '__main__': main()
