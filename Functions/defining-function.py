#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#
# Description:  defining functions
# Reference: Lynda.com, Loops: defining functions
# defining-function.py


def main():
    f1000 = fib(1000)   # Call the function and pass it the 1 required param value
    print(f1000)        # Print the returned result or else nothing will show


# The fibonacci series
def fib(n):

    a, b = 0, 1

    # We could opt to store the results in a list for future dealings
    # First we must create an empty list []
    result = []

    while a < n:
        # print(a, end=' ')

        result.append(a)

        # Basically, the next number in the series is the sum of the previous two numbers
        # Series starts with 0 1
        #   The next number in the series is result of adding 0 and 1
        #   e.g. 0 + 1 = 1
        #       Series is now 0 1 1
        #
        #   Next number would be 1 + 1 = 2:
        #       Series is now 0 1 1 2
        #   The process would continue to the nth number
        a, b = b, a + b

    print()     # Print a new line

    # If we want to do something with the list outside of the function we must return it to whatever
    #   process or method called this function
    #
    # In this instance main() called the fib() function
    return result


if __name__ == '__main__':
    main()

