#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#
# Description:  If and Else
# Reference: Lynda.com, Conditionals: if-else
# if-else.py


def main():

    # Declare vars and initialize
    a, b = 0, 1

    # Create conditional expression
    s = "less than" if a < b else "greater than"
    print(s)

    # Create traditional conditional statement
    if False:
        print("this is true")
    else:
        print("this is false")

if __name__ == '__main__':
    main()
