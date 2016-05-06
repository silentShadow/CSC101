#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#
# Description:  While loops
# Reference: Lynda.com, Loops: while
# while.py


def main():

    # Declare vars and intialize
    a, b = 0, 1

    # Create while loop
    while b < 50:
        print(b, end=' ')

        # Making the Fibonacci series
        a, b = b, a + b


if __name__ == '__main__':
    main()