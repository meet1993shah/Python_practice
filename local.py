def change(b):
	a = 90
	print a
a = 9
print "Before the function call ", a
print "inside change function ", 
change(a)
print "After the function call ", a	


##
print '\n'
def change2(b):
	global a
	a = 90
	print a
print "Before the function call ", a
print "inside change function ", 
change2(a)
print "After the function call ", a		