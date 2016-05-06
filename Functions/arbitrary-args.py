# Finally, the least frequently used option is to specify that a function
#   can be called with an arbitrary number of arguments. These arguments
#   will be wrapped up in a tuple (see Tuples and Sequences). Before the variable
#   number of arguments, zero or more normal arguments may occur.
#


def concat(*args, sep="/"):
    return sep.join(args)


# Args can be unpacked if they are already stored in a list or tuple.
#   A function call is made with the * to unpack the args


def main():
    func = concat("earth", "moon", "sun", "pluto")
    print(func)

    args = [3, 100, 5]
    r = list(range(*args))
    print(r)


if __name__ == '__main__':
    main()


