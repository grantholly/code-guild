user_number = input('gimme a number')

for i in range(user_number + 1):
    if i == 0:
	print(i)
    elif i % 12 == 0:
	print("fizzbuzz")
    elif i % 4 == 0:
	print("buzz")
    elif i % 3 == 0:
	print("fizz")
    else:
	print(i)
