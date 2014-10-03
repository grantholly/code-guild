__author__ = 'grant'

t = 1, 2, 3

print(t)

t = (1, 2, 3,)

print(t)

e = (3, 4)

print(t + e)

print(t * 2)

"""
Tuples are heterogeneous and we can nest them
"""

t = (1, (2,), 'three')

print(t)

print(t[0])

print(t[:-1])

print(t[:2])

print(t.index('three'))

print((t + e + (3,)).count(3))

print(t.count(1))

print((t + e + (3,)).count(3))