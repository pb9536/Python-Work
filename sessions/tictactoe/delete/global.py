x = 3

def some_func(y):
	y = y + 1
	print(y)

some_func(global x)
print(x)
