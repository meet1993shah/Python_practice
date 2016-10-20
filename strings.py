print "Hello World!"
print 'Hello World!'
print 'Here is a line \n splitted in two lines'
s = ''' This is a 
multiline string, so you can
write many lines'''
print s

##
print '\n'
s = "meet shah"
print s.title()
z = s.upper()
print z
print z.lower()
s = "I am A pRoGraMMer"
print s
print s.swapcase()

##
print '\n'
s = "jdwb 2323bjb"
print s.isalnum()
s = "jdwb2323bjb"
print s.isalnum()
s = "HelloWorld"
print s.isalpha()
s = "Hello World"
print s.isalpha()
s = '1234'
print s.isdigit()
s = '12 34'
print s.isdigit()
s = 'Fedora9 is coming'
print s.islower() 
s = 'Fedora9 Is Coming'
print s.istitle()
s = 'INDIA'
print s.isupper()

##
print '\n'
s = "We all love Python"
z = s.split(" ")
print z
t = "We_all_love_python"
z = t.split("_")
print z
m = "Linux is great"
n = m.split(" ")
print "-".join(n)

##
print '\n'
s = "           Hello   My  name      is     Meet                                                 \n        "
print s
print s.strip()
s = "www.foss.in"
print s.lstrip("cwsd.")
print s.rstrip("cnwdi.")
print s.rstrip("cnwdi")

##
print '\n'
s = "faulty for a reason"
print s.find("for")
print s.find("fora")
print s.startswith("fa")
print s.startswith("hi")
print s.endswith("reason")
print s.endswith("world")