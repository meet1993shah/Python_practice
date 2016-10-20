def func(a, b = 5, c = 10):
	print 'a is', a, 'b is', b, 'and c is', c

func(12, 24)
func(12, c = 24)
func(b = 12, c = 24, a = -1)

## The below function will get an error on execution
print '\n'
def func2(a, b = 13, v):
	print a, b, v