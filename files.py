##
fobj = open("love.txt")
print fobj
fobj.close()

##
print '\n'
fobj = open("love.txt")
a = fobj.read()
print a
print fobj.read()
fobj.close()

##
print '\n'
fobj = open("love.txt")
a = fobj.readline()
print a
print fobj.readline()
print fobj.readline()
print fobj.readline()
fobj.close()

##
print '\n'
fobj = open("love.txt")
a = fobj.readlines()
print a
print fobj.readlines()
fobj.close()

##
print '\n'
fobj = open("love.txt")
for x in fobj:
	print x + 'yoyo'
fobj.close()
	
