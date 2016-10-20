data = {'kushal':'Fedora', 'kart_':'Debian', 'Jace':'Mac'}
print data
print data['kart_']
data['parthan'] = 'Ubuntu'
print data
del data['kushal']
print data
print 'parthan' in data
print 'Soumya' in data
print dict((('India', 'Delhi'), ('Bangladesh', 'Dhaka')))
for x, y in data.iteritems():
	print "%s uses %s" % (x, y)

##
print '\n'
data = {}
data.setdefault('names', []).append('Ruby')
print data
data.setdefault('names', []).append('Python')
print data
data.setdefault('names', []).append('C')
print data
print data.get('names', 0)	
print data.get('foo', 0)

##
print '\n'
for i, j in enumerate(['a', 'b', 'c']):
	print i, j

##
print '\n'
a = [4, 3, 2, 20, 56, 102, 32, 10]
for i, j in enumerate(a):
	print i, j

##
print '\n'
a = ['Pradeepto', 'Kushal']
b = ['openSUSE', 'Fedora']
for x, y in zip(a, b):
	print "%s uses %s" % (x, y)
	
