__author__ = 'grant'


b = 'boomshakalaka'

print(len(b))

print(b + '!!!')

print(b * 2)

#print(b / 2)

"""Even though we can use the + and * operators, that doesn't mean
strings support all of the math arithmetic operators.  What's really
happening when you add two strings is you are calling a concat function
that is made for concatenating (not adding) two strings"""

print(b[0])

print(b[-1])

print(b[0:4])

print(b[:3])

print(b[:])

#b[0] = 'z'

b = 'z' + b[1:]

"""strings are immutable meaning that they can't be changed in place.
However, we can overwrite, or create a new string."""

c = 'A\nB\tc'

print(c)

print(ord(c[0]))






