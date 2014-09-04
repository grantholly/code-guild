__author__ = 'grant'


a = 5
b = 2
c = 3.14

print(a + 1)

print(a + 2 * 2)

print((a + 2) * 2)

"""
Gooooing up.  Python converts up to higher complexity data types
before applying operators.
"""

print(a + c)

print(b / a)

print(b / c)

print(a ** 2)

print(a // 2)

print(a % 2)

import math

print(math.floor(2.5))

print(math.floor(-2.5))

print(math.sqrt(4))

"""
floating point accuracy
"""

print(1 / 3)

print(0.1 + 0.1 + 0.1 - 0.3)

import decimal

print(decimal.Decimal('0.1') + decimal.Decimal('0.1') + decimal.Decimal('0.1') - decimal.Decimal('0.3'))

decimal.getcontext().prec = 4

print(decimal.Decimal('1') / decimal.Decimal('7'))
