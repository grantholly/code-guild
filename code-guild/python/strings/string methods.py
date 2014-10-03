__author__ = 'grant'

s = 'super string'

print(len(s))

print('-' * 10 + s + '-' * 10)

print('s' in s)

print('k' in s)

print('ring' in s)

print('supe' + 'z' in s)

print(s[0:12:2])

print(s[::-1])

print(s[12:5:-1])

print(str(10) + s)

print(repr(10))

print(ord('a'))

print(chr(97))

d = 'duper'

print(s + d)

print(s[:6] + d + s[5:12])

print(s.replace('u', 'oo'))

print(s.capitalize())

print(s.upper())

print(s.swapcase())

print(s.lower())

print(s.split())

s = 'super/string'

print(s.split('/'))

s = 's*u*p*e*r* *s*t*r*i*n*g'

print(s.split('*'))

s = 'super string'

print(' '.join(['super', 'string']))

print(s.endswith('g'))

print(s.startswith('z'))



print(s.find('str'))


