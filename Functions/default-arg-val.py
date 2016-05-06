#
#
# Description: It is also possible to define functions with a variable number of arguments.
#   There are three forms, which can be combined.
#
#   Default Argument Values
#   Keyword Arguments - see keyword-args.py
#   Arbitrary Argument Lists - see arbitrary-args.py


# Default Argument Values
# The most useful form is to specify a default value for one or more arguments.
#   This creates a function that can be called with fewer arguments
#   than it is defined to allow. For example:
#
def ask_ok(prompt, retries=3, complaint="Yes or no, please"):
    while True:
        ok = input(prompt)

        if ok in ('y', 'ye', 'yes'):    # in: Determine if sequence contains that value
            return True

        if ok in ('n', 'no', 'nop', 'nope'):
            return False

        retries -= 1

        if retries < 0:
            raise OSError("Unruly user is here!")
        print(complaint)


# The default value is evaluated only once.
#   This makes a difference when the default is a mutable object
#   such as a list, dictionary, or instances of most classes.
#
#   For example, the following function accumulates the arguments
#       passed to it on subsequent calls:
#
def f(a, L=[]):
    L.append(a)     # Add what was passed to the list 'L'
    return L


def main():
    # ask = ask_ok("Do you want to quit? ")
    # print(ask)

    print(f(1))
    print(f(2))
    print(f(3))


if __name__ == '__main__':
    main()

