__author__ = 'grant'


number = input('gimme a number') + 1
primes = []

for i in range(2, number):
    prime = True
    for j in range(2, i - 1):
        if i % j == 0:
            prime = False
    if prime is True:
        primes.append(i)

print(primes)



