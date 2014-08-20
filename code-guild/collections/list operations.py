__author__ = 'grant'


l = [1, 2, 3, 4]

print(len(l))

print(l[0], l[1], l[2], l[3])

three = 3

"""
unlike strings, lists are arbitrary ordered sequences
of things that are heterogeneous and they are mutable.
"""

l = ['one', 2, three, 4]

l[2] = 3

print(l)

l[:2] = ['first', 'second']

print(l)

"""
Let's enter the matrix!
"""

matrix = [[10, 20], [30, 40]]

print(matrix)

print(matrix[0])

print(matrix[0][0])

print(matrix[1][0])

print(len(matrix[0]))

"""
lists have their own methods as well
"""

l.append('five')

six = 'six'

print(l)

l.reverse()

print(l)

l.extend(six)

print(l)

l.reverse()

print(l)

l.pop()

print(l)

l.pop(0)

print(l)

l.remove('i')
l.remove('s')

print(l)

l.extend(l)

print(l)

print(l.count('first'))

print(list(l))

