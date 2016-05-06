#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#
# Description:  enumerating iterators
# Reference: Lynda.com, Loops: enumerating iterators
# enumerating iterator.py


def main():

    # Declare file handler to open file
    fh = open("lines.txt")

    # This will create a double iterator of sorts
    # i will iterate for n lines
    # line will iterate over each line
    for i, line in enumerate(fh.readlines()):
        print(i, line, end='')

    fh.close()

    if fh.closed:
        print("\nfile closed successfully")
    #
    #
    #
    # Enumerate over a string
    s = "this is a string, duh"

    for i, x in enumerate(s):
        if x == "s": print("index {} of the string '{}' is a(n) s".format(i, s))

    #
    #
    #
    # Enumerate over items in a list
    a = ["Mary", "had", "a", "little", "lamb"]

    for i, word in enumerate(a):
        print("Line {}, {}".format(i, word))

if __name__ == '__main__':
    main()
