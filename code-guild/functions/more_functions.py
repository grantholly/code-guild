def f(x):
    #local x
    x = 99

#global y
y = 88

f(y)
print(y)

#arguments work like local variables for the passed in objects
#when the function is called.  The arguments exist in the function
#scope when the function is called.

def g(a, b):
    a = 2
    b[0] = 'changed'

x = 1
l = [2, 3]

g(x, l)

#watch out for changing mutable objects when they are
#passed in as arguments.  Any in-place changes may affect
#other functions

g(x, l[:])

#pass in a copy of l

def r(a, b, c):
    print(a, b, c)

#arguments are matched positionally left to right
#to the passed in objects

r(1, 2, 3)

def t(c=3, a=1, b=2):
    print(a, b, c)

#arguments can be passed by keyword in any order

t(b=1, a=3, c=2)

t(1, 3, c=2)

#arguments if not called by keyword will be positionally matched

t(1)

#keyword arguments can be used to assign default values

def v(*args):
    for i in args:
	print(i)

#*args collects any number of arguments and passes them
#into the function inside a tuple

v(1)

v(2, 3, 4, 5)

v('a', 'b', 'c')

#**kwargs allows a function to take any number of keyword
#arguments and passes them into the function in a dictionary

def u(**kwargs):
    print(kwargs)

u(name='max', age=26, hobbies=["sailing", "gardening"])

#you can use the dictionary views and methods to loop through
#the different iteration contexts in kwargs

def j(a, b=2, *stuff, **things):
    a += 1
    return(a * b, stuff, things)

j(2, 'blake', 'chaz', popped_collar=True, major='business')

#functions can use any mixture of positional, keyword, *args
#or **kwargs



