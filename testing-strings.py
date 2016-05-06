#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
##+
##+ Strings
##+ Ref. Python Help: STRINGS
##+ Strings.py


stringLiteral = '''\
This is a
multi-line string
literal. This is
using triple quotes.
AKA: triplequotedstring
'''

stringRaw = r'c:\\users\student\desktop\name'
stringNotRaw = 'c:\\users\student\desktop\name'

print(stringLiteral)
print("""\
Printing raw strings with 'r' in front of the string:
    {}
Without 'r' it would look like this:
    {}
""".format(stringRaw, stringNotRaw))
