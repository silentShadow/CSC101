check_point = {
'6.1 What are the benefits of using a function?' : '\n\tcode reusability and simplification \n',

'6.2 How do you define a function? How do you invoke a function?' : '\n\tdef name(params):body, m = main() \n',

'6.3 Can you simplify the max function in Listing 6.1 by using a conditional expression?' : '\n\t   \n',

'6.4 True or false? A call to a None function is always a statement itself, but a call to a value-returning function is always a component of an expression.' : '\n\tTrue \n',

'''\
6.5 Can you have a return statement in a None function? Does the return statement in the following function cause syntax errors?
def xFunction(x,y):
    print(X+y)
    return
''' : '\n\tYes. No  \n',

'6.6 Define the terms function header, parameter, and argument' : '\n\tHeader starts with def ends with :. params are vars, args are vals to params  \n',

'6.7' : '\n\t  \n',

'6.8' : '\n\t  \n',

'6.9' : '\n\t  \n',

'6.10' : '\n\t  \n',

'6.11 Compare positional arguments and keyword arguments' : '\n\tPositional args: specific order, kywd args: name=val \n',

'''\
6.12 Suppose a function header is as follows:
def f(p1, p2, p3, p4):
Which of the following calls are correct?
a. f(1, p2 = 3, p3 = 4, p4 = 4)
b. f(1, p2 = 3, 4, p4 = 4)
c. f(p1 = 1, p2 = 3, 4, p4 = 4)
d. f(p1 = 1, p2 = 3, p3 = 4, p4 = 4)
e. f(p4 = 1, p2 = 3, p3 = 4, p1 = 4)
''' : 'a, d, e',

'6.13 What is pass-by-value?' : '\n\tpassing the reference of a var to a functions param \n',

'6.14 Can the argument have the same name as its parameter?' : '\n\tYes  \n',

'''\
6.15 Show the result of the following programs: 
''' : 
'''\
   a.  2
    
    b.  
        2
        2 4 
        2 4 8
        2 4 8 16
        2 4 8 16 32
        
    c.  Before the call, variable times is 3
        n =  3
        Welcome to CS!
        n =  2
        Welcome to CS!
        n =  1
        Welcome to CS!
        After the call, variable times is 3
        
    d.  i is 1
            1
        i is 2
            2
        i is 3
            nothing
        
''',
'''\
6.17 What is the printout of the following code?

def function(x):
    print(x)
    x = 4.5
    y = 3.4
    print(y)
x = 2
y = 4
function(x)
print(x)
print(y)
''': 
'''\
function(x) = 2, 3.4
print(x) = 2
print(y) = 4
''',

'''\
def f(x, y = 1, z = 2):
    return x + y + z
print(f(1, 1, 1))
print(f(y = 1, x = 2, z = 3))
print(f(1, z = 3))
''' :
"3,  6,  5",

'''\
6.18 What is wrong with the following code?
1 def function():
2   x = 4.5
3   y = 3.4
4   print(x)
5   print(y)
6
7 function()
8 print(x)
9 print(y)
''':
"lines 8 and 9 will raise NameError as not being defined",

'''\
6.19 Can the following code run? If so, what is the printout?
x = 10
if x < 0:
    y = -1
else:
    y = 1
    
print("y is", y)
''':
"It runs, 1",

'''\
6.20 Show the printout of the following code:
def f(w = 1, h = 2):
    print(w, h)
f()
f(w = 5)
f(h = 24)
f(4, 5)
''' :
'''\
1, 2
5, 2
1, 24
4, 5
''',

'''\
6.21 ID and correct the errors in the following code
1 def main():
2   nPrintln(5)
3
4 def nPrintln(message = "Welcome to Python!", n):
5   for i in range(n):
6       print(message)
7
8 main() # Call the main function
''' :
"Line 4 should read:  def nPrintln(n, message = 'Welcome to Python!')",

'''\
6.22 What happens if you define two functions in a module that have the same name?
''' :
"The most recent will get loaded",

'''\
6.23 Can a function return several values?  Show the printout of the following code:
1 def f(x, y):
2   return x + y, x - y, x * y, x / y
3
4 t1, t2, t3, t4 = f(9, 5)
5 print(t1, t2, t3, t4)
''' : 
"Yes, 14, 4, 45, 1.8" 

}


for k, v in sorted(check_point.items()):
    print(k, v)