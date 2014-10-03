__author__ = 'grant'

a = set('abc')
b = set('xyz')
c = set('cxq')

print('c' in a)

print('q' in a)

print(a - b) #difference

print(a | c) #union

print(a & c) #intersection

print(a.intersection(c))

print(a > c) #a is a superset of c?

print(a < c) #a is a subset of c

b.add('qrs')

print(b)

b.update('q', 'r')

print(b)

b.remove('qrs')

print(b)


