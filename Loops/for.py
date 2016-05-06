#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#
# Description:  For loops
# Reference: Lynda.com, Loops: for
# for.py


def main():
    fh = open("lines.txt")

    for line in fh.readlines():

        # Default: print will add a newline even if the file doesn't have one
        # We need to change that
        # print(line, end='')
        print(line, end='')

    fh.close()

    if fh.closed:
        print("\nfile closed successfully")

if __name__ == '__main__':
    main()
