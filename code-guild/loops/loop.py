#####################################
#------------while loops------------#
#####################################
#basic while loop
#these two variables track where we are in the loop
#and where we are going
a = 0
b = 10

while a < b:
    print(a)
    a += 1

#these must be reset because the loop above
#sets the values of the global a and global b
a = 0
b = 10

#we will break at seven (optional)
while a < b:
    print(a)
    a += 1
    if a == 7:
	break

a = 0
b = 10

#the continue will make our loop go back to the top
#and evaluate our looping condition.  (optional)
while a < b:
    print(a)
    a += 1
    if type(a) == 'int':
	continue
    if a == 9:
	break

a = 0
b = 10

#the else clause runs if we don't hit the break
#and we exit the loop normally
while a < b:
    print(a)
    a += 1
    if a == 'g':
	break
else:
    print('all done looping')

############################
#-------for loops----------#
############################

#simple for loop with an iterator and an iterable
for number in [1, 2, 3]:
    print(number)

#strings are sequence objects, so we can loop through them
for letter in 'string':
    print(letter)

#works for tuples too
for element in (1, 2, 'a'):
    print element

#works on sets, even though they are un-ordered
for element in set([1, 2, 2, 3, 4, 4]):
    print(element)

#sets are perfect for looping
things = [1, 'two', [3, 4], (5,), {6: 'six'}]
for thing in things:
    print(thing)

#because dictionaries are accessed by their keys,
#returning i will return the keys of the dictionary
#that is is searching
for i in {'a': 1, 'b': 2, 'c': 3}:
    print(i)

d = {'a': 1, 'b': 2, 'c': 3}

#dictionaries have a lot of very helpful built-in methods
#to handle iteration on them
for key in d.keys():
    print(key)

for value in d.values():
    print(value)

for item in d.items():
    print(item)

l = [(1, 2), (3, 4), (5, 6)]
v = [('a', 'b'), ('c', 'd'), ('e', 'f')]
b = [1, 2, 3, 4]
x = ['a', 'b', 'c', 'd']
#looping can be used to do in-place assignment
#to mutable objects like lists
for i in b:
    i += 1
    print(i)

print(b)

#print 1a, 1b, 1c, 1d, 2a...
#b is the outer loop and x is the inner loop
for i in b:
    for j in x:
	print(i, j)

for (key, value) in {'a': 1, 'b': 2, 'c': 3}.items():
    print("{} is the key for value {}").format(key, value)

#print just the first element of the tuples in l
for (i, j) in l:
    print(i)

#print just the second element of the tuples in l
for (i, j) in l:
    print(j)

#both while loops and for loops support conditional logic
for i in b:
    if i % 2 == 0:
	print(i)

#print the second element of each tuple in the loop
for tuple in v:
    print(v[0])

#looping with conditional logic checked each time
#through the loop.  The last optional else runs just
#like in a while loop if the loop exits normally
#and does not run into a break statement
letters = "qwertyuiopasdfghjklzxcvbnm"

for letter in letters:
    if letter in ['a', 'e', 'i', 'o', 'u']:
	print("%s is a vowel") % letter
    else:
	print(letter)
else:
    print("no more letters left")
