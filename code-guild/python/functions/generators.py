def fibonnacci():
    a, b = 0, 1
    while True:
	yield b
	a, b = b, a + b

fib = fibonnacci()

fib.next()
fib.next()
fib.next()

"""
the first 10 fibonnacci numbers
"""
fibs = []
for i in range(1, 11):
    fibs.apend(fib.next())

[fib.next() for i in range(1, 11)]

"""
we can see that the generator is keeping track of where it left off
everytime we need a new fibonnacci number, we can just call next()
on the generator object or function

this can be a big performance boost in that, unlike a traditional
iteration through an iterable object, with a generator, the iterable
object never has to be defined before we can use the generator.  This
means that we don't have to store in memory really large collections
like lists or tuples
"""

powers = (i**2 for i in range(100) if i % 2 == 0)

"""
just like list comprehensions, a generator can be used to create
objects on the fly
"""
