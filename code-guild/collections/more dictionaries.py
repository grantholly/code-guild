__author__ = 'grant'

c = dict(name='bill', age=21, occupation='student')

print(c)

e = dict([('name', 'jim'), ('age', 21), ('occupation', 'student')])

print(e)

d = dict(zip([1, 2, 3, 4], ['first', 'second', 'third', 'fourth']))

print(e.keys())

print(e.values())

print(d)

keys = {1: 1, 2: 2, 3: 3, 4: 4}
values = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
f = dict(zip(keys.keys(), values.values()))

print(f)

print(f.items())

"""
Dictionary views like keys, items, and values can be treated as sets
"""

three = 3
b = {'a': 'alpha', 'b': 2, 'c': three, 'dee': ['last']}
a = dict(a=1, b=2, c=3, d=4)

print(a)

z = a.keys()

print(z)

y = a.values()

print(y)

print(a.keys() & b.keys())

print(a.keys() & 'b')

print(z[:2] & b.keys())

print(b.values() | a.values())

print(b.items() | a['a'])











