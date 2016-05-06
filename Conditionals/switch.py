#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#
# Description:  Python version of switch: choices()
# Reference: Lynda.com, Conditionals: switch
# switch.py


def main():

    # Declare a dictionary with possible values
    # Could assign actions to take if an option is selected
    choices = dict(
        one = "one",
        two = "two",
        three = "three"
    )

    x = "two"

    print(choices[x])


if __name__ == '__main__':
    main()
