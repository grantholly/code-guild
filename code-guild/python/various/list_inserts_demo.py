l = ['the', 'quick', 'brown', 'fox']

print(l.index('the'))

l[l.index('the')] = 'happy'

print(l)

l.insert(0, 'dog')

print(l)
