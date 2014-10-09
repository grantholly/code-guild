import time

def mydecorator(func):
    def inner(*args, **kwargs):
        print("let's list the arguments")
        return func(*args, **kwargs)
    return inner


@mydecorator
def first(*args):
    for arg in args:
        print"argument number %d" % arg

print(first(1, 2, 3, 4))

"""
    This is very similar to saying
    first(*args) = mydecorator(first(*args))

    1. mydecorator gets made
    2. mydecorator creates the inner function,
       that, like a place holder, could be any function
    3. step into inner function
    4. returns the func argument which could be any function
    5. the function first gets made
    6. function first is enclosed by first meaning
       first is an argument to the decorator function"""

def addone(func):
    print(func.__class__)
    return func() + 1


def doubleit(func):
    print(func.__class__)
    return func * 2


@doubleit
@addone
def five():
    return 5

print(five)

"""First five() gets decorated with addone(), then following inside out, gets decorated a second time
with doubleit().  If it were the other way around, the program would print out 11.  Addone() takes
a function object of five() and then encloses it.  This returns the initial int evaluation of five(),
then the enclosing evaluation of addone().  After computing addone(), we are left with an int returned.
Doubleit() then takes the int object returned by addone(five()) and encloses it."""

def countit(func):
    def inner(*args, **kwargs):
        inner.counter += 1
        return func(*args, **kwargs)
    inner.counter = 0
    return inner


@countit
def f():
    print("f ran")

f()
f()
f()
print(f.counter)


def timeit(func):
    def inner(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        elapsed = time.time() - start
        print(str(elapsed)) + " seconds."
        return ret
    return inner


@timeit
def wastetime():
    print"Here's to wasting "

wastetime()








