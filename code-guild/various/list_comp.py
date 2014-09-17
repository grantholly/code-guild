#results = []
#for i in range(11):
#    results.append(i)

results = [x for x in range(11)]

l = [x * y for x in range(11) for y in range(1, 6)]
#print(l)

def double_it(n):
    return n * 2

l = [double_it(x) for x in range(11)]

#print(l)

l = list(map((lambda x: x * 2),(range(11))))

print(l)

secret = 'dog'
element = 'j'

mask = ['_{}'.format(element) for x in secret]

print(mask)
