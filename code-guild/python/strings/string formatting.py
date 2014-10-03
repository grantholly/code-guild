__author__ = 'grant'

print('The quick %s %s jumped over the %s dog' % ('brown', 'fox', 'lazy'))

print('the %d musketeers' % 3)

thingyousay = 'ho'

print('I say hey, you say %s' %thingyousay)

print('%s is actually a string' % 23)

#expressions
#s - string
#r - uses __repr__
#c - single char
#d - decimal number
#i - integer
#x - hexidecimal integer
#e - floating exponent point number
#f - floating point number

number = 1234

print('start with %d, then add some trailing padding with %-6d, and finish up with leading padding %06d' % (number, number, number))

number = 1.23456789

print('%e, %f' % (number, number))

greeting = """
Hey %(name)s!
You look like you could use a %(drink)s.
"""
variables = {'name': 'Wanda', 'drink': 'pint of porter'}
print(greeting % variables)

print('%(n)s %(x)s' % {'n': 1, 'x': 2})

"""building strings adn returning them from the string object"""

template = '{0}, {1} and {2}'
print(template.format('1st', '2nd', '3rd'))

template = '{first}, {second} and {third}'
print(template.format(first='1', second='2', third='3'))

template = '{first}, {0} and {third}'
print(template.format('second', first='first', third='third'))

import sys

print('My {1[machine]:<8} runs {0.platform:>8}'.format(sys, {'machine': 'computer'}))

print('My %(machine)-8s runs %(platform)8s' % dict(machine='computer', platform=sys.platform))


