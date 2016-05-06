import os

"""\
exec(compile("print('hello')",'test','exec'))
exec(compile("print(os.name)",'test','exec'))    
"""

hidden_val = "secret message here"


def danger(name):
    """\
    This is a really dangerous function
    """
    fh = open(name)
    fh.readlines()


user_func = eval(input("Give me something \n> "))

print(user_func)