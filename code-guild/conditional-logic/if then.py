__author__ = 'grant'

a = 10

if a / 10 == 0:
    print('variable a is probably 10')

if True:
    print('tis true')

if 1:
    print('its a one')

if 't':
    print('the non-empty is treated as true')

if a / 3 == 0:
    print('variable a is probably 3')
else:
    print('variable a is something else')

weather = 'rainy'

if weather == 'sunny':
    __doc__ = "this tests if the weather variable is nice out" \
              "this is also a doc string just for the if statement."

"""
ternary operators are a nice shortcut for writing if statements,
but remember, always air on the side of readability.  Complex
ternary statements can be hard to debug and understand later.
"""

x = 10 if 's' in 'string' else 5

print(x)


