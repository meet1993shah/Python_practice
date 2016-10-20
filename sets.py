a = set('abcthabcjwethddda')
print a

##
print '\n'
a = set('abracadabra')
b = set ('alacazam')
print a
print b
print a - b
print a | b
print a & b
print a ^ b

##
print '\n'
a = set('abcthabcjqwethddda')
print a
a.add('p')
print a
print a.pop()
print a.pop()
print a