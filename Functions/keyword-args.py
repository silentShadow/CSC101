# This parrot function is accepting one required param (argument), voltage
#   and 3 optional args that have default values: state, action, type
#


def parrot(voltage, state='a stiff', action='voom', types='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", types)
    print("-- It's", state, "!")

    return None


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any {}?".format(kind))
    print("-- Sorry, all out of {}".format(kind))

    print("{:-^60}".format(" arguments "))

    for arg in arguments:
        print(arg)

    print("{:-^60}".format(" keywords "))

    keys = sorted(keywords.keys())

    for kw in keys:
        print("{} : {}".format(kw, keywords[kw]))


def main():
    onePos = parrot(1000)                               # 1 positional arg
    oneKywd = parrot(voltage=1000)                      # 1 kywd arg
    twoKywd = parrot(voltage=1000, action="WOOSH")      # 2 kywd args
    opt2kywd= parrot(action="WOOSH", voltage=2000)      # 2 kywd args
    thrPos = parrot("100", "bereft of life", "jump")    # 3 positional args
    oneKywdOnePos = parrot("thousand", state="dead")    # 1 positional, 1 kywd
    print(onePos)
    print(oneKywd)
    print(twoKywd)
    print(opt2kywd)
    print(thrPos)
    print(oneKywdOnePos)

    cheeseshop("Swiss", "It has a lot of holes", "A bunch of holes", owner="Jonny Bravo", client="John Cena")



if __name__ == '__main__':
    main()
