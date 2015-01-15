"""
traditional looping as we know it
1. create an object to store the elements as we iterate
2. loop through a collection
3. append those elements to our result
4. return or display the results
"""
results = []
numbers = [1,2,3,4,5,6,7]

for number in numbers:
    print results.append(number)

print results

"""
comperable list comprhension

wow! Just a single line of code.  
"""
results = [number for number in numbers]

"""
you can also add additional logic
"""
evens = [number for number in numbers if number % 2 == 0]

"""
or the more traditional way
"""

numbers = [1,2,3,4,5,6,7,8,9,10]
evens = []

for number in numbers:
    if number % 2 == 0:
	evens.append(number)

print(evens)

"""
applying function calls too!
"""
evens = [str(number) for number in numbers if number % 2 == 0]

"""
this works for dictionaries too
"""
d = {k: v for k, v in zip(range(1, 11), range(1, 11))}

evens_only_please = {k: v for k, v in zip(range(1, 11), range(1, 11)) if k % 2 == 0}

now_with_functions = {str(k): v for k, v in zip(range(1, 11), range(1, 11)) if k % 2 == 0}

def favorite_number(n):
    if n in (2, 3, 5, 7, 11, 13, 17, 19):
	return str(n) + " is a favorite"

favorites = [favorite_number(i) for i in range(1, 21) if i % 3 == 0]

"""
comprehensions are very efficient ways to create collection objects
we reduce the number of external objects that the collection creation
requires, plus, we build the object on the fly rather than performing
work in each loop iteration.

watch out for very complex comprehensions because it can make your
code more difficult to read, and hence, debug or extend later
"""
