def yell(word):
    print(word.upper())

mad = yell

mad('hey there')

#fucntions can be called indirectly through references

def f(x, y, z):
   return x - y - z

f(30, 20, 10)

f = (lambda x, y, z: x - y - z)
f(30, 20, 10)

def greeting():
    title = 'sir'
    say = (lambda x: title + ' ' + x)
    return say

hi = greeting()

hi('Grant')

#lambda is used to create anonymous functions inline
#without requiring a def statement

import sys
from tkinter import Button, mainloop

x = Button(
	text = 'push this button',
	command = (lambda: sys.stdout.write('you pushed the button\n'))
	)

x.pack()
mainloop()

#here a lambda is being used as a callback function with the
#tkinter python module for GUIs.  When the button is pushed,
#a lambda expression runs and generates a message.

def f(x, func):
    x += 1
    return func(x)

def g(y):
    y *= 2
    return y

f(2, g)

#in this example, g is being used a callback function with f.
#Once f has finished computing x, x is then passed into the
#callback function g which further processes x, which is now
#associated with the local argument y and the scope of g.
