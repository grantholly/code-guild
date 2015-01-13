def myfunction():
    print("my function is working")

myfunction()
myfunction()

def addone(number):
    return number + 1

addone(2)
addone(4)

#print sends values to the standard output
#return sends the returned object back to the caller
#this returned object can be reused by the program

def doubleit(x):
    return x * 2

def squareit(j):
    return j ** 2

#functions can be can be chained together when they return objects

squareit(doubleit(addone(2)))

#each function returns an object to the surrounding function
#that can operate on that returned object

#global x
x = 5

def f(n):
    #local x
    x = 1
    return x + n

#functions introduce new function scopes to the program

f(2)

#the global reserved word allows us to import a global
#variable from the global scope into our function scope

def g(n):
    global x
    return x + n

g(2)

#remember LEGB!  This is how python looks up references
#local, enclosing, global, built-in

z = 100

def t():
    z = 20
    def j():
	print(z)
    j()

#Python finds z in the enclosing scope of j

t()

def s():
    z = 30
    def q():
	print(z)
    return q()

#the function object q is being returned

test = s()

#test is now a reference to the function object s()

test

#s is a function object that reurns the q function object

test()

#this is a function call from test --> s() --> q()

def r():
    z = 40
    def e():
	nonlocal z
	z += 1
    return e

#the nonlocal reserved word allows the local scope of e()
#to import from the enclosing scope of r()
#this is Python 3 only

r()

def y():
    h = 10
    return z * h

#here the global z is being referenced inside scope of y()
#but it is not created in the scope of y() because there
#is no assignment like z = 10

y()
