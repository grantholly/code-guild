a = 1
b = 21

while b >= a:
    b -= 1
    if b == 15:
	print(b)
	b -= 2
    if b == 10:
	print("halfway done")
	b -= 2
    if b == 5:
	print(b)
	b -= 2
    print(b)
else:
    print("all done") 
