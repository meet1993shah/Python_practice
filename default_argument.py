def test(a, b=-99):
	if a > b:
		return True
	else:
		return False

print test(12, 23)
print test(12)	

##
print '\n'
def f(a, data=[]):
	data.append(a)
	return data

print f(1)
print f(2)
print f(3)	

##
print '\n'
def g(a, data=None):
	if data is None:
		data = []
	data.append(a)
	return data

print g(1)
print g(2)		