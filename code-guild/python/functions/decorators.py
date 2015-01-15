import time
import hashlib
import pickle
from itertools import chain

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
       first is an argument to the decorator function
"""

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

"""
First five() gets decorated with addone(), then following inside out, gets decorated a second time
with doubleit().  If it were the other way around, the program would print out 11.  Addone() takes
a function object of five() and then encloses it.  This returns the initial int evaluation of five(),
then the enclosing evaluation of addone().  After computing addone(), we are left with an int returned.
Doubleit() then takes the int object returned by addone(five()) and encloses it.
"""

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

cache = {}

def is_obsolete(entry, duration):
    """
    this function checks if a cached function signature
    should be evicted from the cache
    """
    return time.time() - entry["time"] > duration

def compute_key(function, args, kwargs):
    """
    this function takes a function and all of its arguments
    to create a cryptographic hash of the function signature
    """
    key = pickle.dumps((function.func_name, args, kwargs))
    return hashlib.sha1(key).hexdigest()

def memoize(duration=10):
    def _memoize(function):
	def __memoize(*args, **kwargs):
	    key = compute_key(function, args, kwargs)

	    # if the function signature isn't in the cache
	    if key in cache and not is_obsolete(cache[key], duration):
		print("that function signature is in the cache")
		return cache[key]["value"]

	    # if we can't serve from the cache
	    result = function(*args, **kwargs)
	    
	    # now cache the result
	    cache[key] = {"value": result, "time": time.time()}
	    
	    return result
	return __memoize
    return _memoize

# memoize the function and cache for 10 seconds
memoize(10)
def calculation(a, b):
   go_to = range(len(b))
   for i in go_to:
	go_to[i] += a
   return go_to
