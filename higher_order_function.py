def high(func, value):
	return func(value)

lst = high(dir, int)
print lst[-3:]
print lst

##Example of map function
print '\n'
lst = [1, 2, 3, 4, 5]
def square(num):
	"Returns the square of a given number."
	return num * num

print [square(x) for x in lst]
print map(square, lst)