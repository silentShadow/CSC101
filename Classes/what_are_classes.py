'''\
rev: 1
author: silentshad0w
description: what are classes and how do you use them to create objects
reference: https://www.youtube.com/watch?v=HwSRr-VpAbY&index=26&list=PLlgoYPTU6ljCEggReCMF0m0760QTot9Qz
reference: https://pythonspot.com/en/objects-and-classes/
reference:
things to know:  
    namespace:
        - mapping from names to objects
        - most are implemented as Python dictionaries
        - examples would be the set of built-in names containing functions like abs(); global names in a module; 
            local names in a function
        - no relation between names in different namespaces: example:
            2 different modules can define a function maximize without confusion
        - created at different moments
        - have different lifetimes
            + the namepsace containing the built-in names is created when the Python interpreter starts
            + built-in names live in a module; builtins
        - local namespace for a function is created when the function is called; deleted when the function returns
            or raises and Exception that the function does not handle
    
    scope:
        - a textual region of a Python program where a namespace is Directly Accessible (DA)
        - determined statically; used dynamically
        - there are at least 3 nested scopes whose namespaces are DA
            + innermost scope, searched first, contains local names
            + scope of any enclosing functions, nearest enclosing scope containing nonlocal, but nonGlobal names
            + next-to-last scope contains the current module's global names
            + outermost scope, searched last, is the namespace containing built-in names, builtins
        - if a name is declared global, then all references/assignments go directly to the middle scope containing
            the module's global names
            + to rebind vars found outside of the innermost scope, the nonlocal statement can be used
                ^ if declared nonlocal, vars are read-only
        - if no global statement is in effect, assignments to names always go into the innermost scope
        - assignments do not copy data - they just bind names to objects
        - all operations that introduce new names use the local scope;
            + import statements and function definitions bind the module or function name in the local scope
        - global:
            + indicates that vars live in the global scope and should be rebound there
        - nonlocal:
            + indicates that vars live in an enlcosing scope and should be rebound there
            
def scope_test():
    def do_local():
        spam = "local spam"
        
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
        
    def do_global():
        global spam
        spam = "global spam"
        
    spam = "test spam"
    do_local()
    print( "After the local assignment: {}".format( spam))
    
    do_nonlocal()
    print( "After nonlocal: {}".format( spam))
    
    do_global()
    print( "After global: {}".format( spam))
    
    
scope_test()
print( "In global scope: {}".format( spam))
print()
print()
          
          
    attribute:
        - any name following a dot; dot-notation
        - z.real: real is attribute of z module object
        - os.path: path is the attribute of the os module object
        - can be read-only or writable:
            + module.age = 43   # give 43 to age attribute
            + del module.age    # del the age attribute
'''






'''\
Class objects support 2 kinds of operations: attribute references and instantiation

'''
class EasyClass:
    '''Simple example class showing attribute references'''
    i = 12345
    
    def f( ):
        return 'hello, world'
        
        
a = EasyClass.i             # Valid atribute reference
b = EasyClass.f             # Valid atribute reference
d = EasyClass.__doc__       # Valid atribute reference
e = EasyClass.i = 32768     # Valid atribute assignment

for i in range( 1,3):
    print( b())
print( a, d, e, sep='\n')
print()



'''\
Class instantiation uses function notation.
Pretend that the class object is a parameterless function that returns a new instance of the class 

the instantiation operation, calling a class object, creates an empty object
    ^ many classes like to create objects with instances custmoized to a specific initial state
    ^ a class may define a special method named __init__()
        def __init__( self):
            self.data = []
    ^ when a class defines an __init__() method, class instantiation automatically invokes __init__()
        for the newly-created class instance
'''
x = EasyClass()             # The EasyClass is now instantiated



class Complex:
    def __init__( self, realpart, imagpart ):
        self.realpart = realpart
        self.imagpart = imagpart
        
z = Complex( 3, -4.5)
z.realpart
z.imagpart






'''\
Classes and instance vars:
    - instance vars are for data unique to each instance
    - class vars are for attributes and methods shared by all instances of the class
    
'''

class Dog:
    kind   = 'canine'               # Class var shared by all instances
    #tricks = []                    # This list will be shared by all instances
    
    def __init__( self, name):
        self.name = name            # instance var unique to each instance
        self.tricks = []            # This is the proper place for the list so each one will be unique
        
    def add_trick( self, trick):
        self.tricks.append( trick)
        
a = Dog( 'Fido')
b = Dog( 'Buddy')

a.kind                          # Shared by all dogs, all instances
b.kind                          # Shared by all dogs, all instances
a.name                          # Unique to a
b.name                          # Unique to b

a.add_trick( 'play dead')       # Call the add_trick() method with 'play dead' arg
b.add_trick( 'speak')

a.tricks                        # Reference the attribute of the unique instance
b.tricks                        # Reference the attribute of the unique instance




class Bag:
    def __init__(self):
        self.data = []
        
    def add( self, x):
        self.data.append( x)
        
    def add_twice( self, x):
        self.add( x)
        self.add( x)


h = Bag( )
h.add( 5)
h.add_twice( 10)
print( h.data )
print()



'''\
Inheritance

SYNTAX:
    class DerivedClassName( BaseClassName):     # Or ( module.attribute)
        suite-1
        ...
        suite-n
'''




'''\
Reversing objects using an iter()

    - 
'''

class Reverse:
    '''Iterator for looping over a sequence backwards'''
    def __init__( self, data):
        self.data = data
        self.index = len( data)
        
    def __iter__( self):
        return self
        
    def __next__( self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[ self.index]
        
        
rev = Reverse( 'spam')
for ch in rev:
    print( ch, end='')
print()





'''\
Generator Expressions:

'''
# Sum of squares
print( sum( i*i for i in range( 10))) 

l1 = [10, 20, 30]
l2 = [7, 5, 3]
print( sum( x*y for x,y in zip( l1, l2)))




'''\
Factories:

reference: https://pythonspot.com/en/factory-method/
'''

class Car(object):
    def factory( type):
        if type == 'racecar':
            return RaceCar()
        if type == 'van':
            return Van()
            
    factory = staticmethod( factory)
    
    
class RaceCar(Car):
    def drive( self): print( 'Driving the racecar')

class Van(Car):
    def drive( self): print( 'Driving the van')
    
    
obj = Car.factory('racecar')
obj.drive()

