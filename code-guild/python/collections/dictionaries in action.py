__author__ = 'grant'

d = {'key': 'value'}

print(type(d))

"""
Unlike lists, dictionary elements are accessed by their keys
not by their offset or index.
"""

d = {1: 'one', 2: 'two', 3: 'three', 4: ' four'}

print(d[1])

#print(d[0])

"""
Dictionaries are not sequences, so objects don't get stored and accessed
by offset or index.  Keys must be immutable objects.
"""

d[5] = 'five'

print(d)

d.pop(3)

print(d)

"""
Nesting lists and other dictionaries.  Such wow!
"""

d['m0'] = [1, 2]

d['m1'] = [[10, 20], [30, 40]]

print(d)

d['d1'] = {}

d['d1'] = {'key': 'value'}

print(d)

other = {'this': 'that', 10: 1024}

d.update(other)

print(d)

"""
Time for some methods.
"""

print(d.items())

print(d.keys())

print(d.get(4))

print(d.popitem())

print(d)





