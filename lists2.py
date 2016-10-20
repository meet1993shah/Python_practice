a = [23, 45, 1, -3434, 43624356, 234]
print a
a.append(45)
print a
a.insert(4, 100)
print a
a.insert(12, 2)
print a
print a.count(45)
a.remove(234)
print a
a.reverse()
print a
b = [45, 56, 90]
a.append(b)
print a
print a[-1]
a.extend(b)
print a
print a[-1]
a.sort()
print a
del a[-1]
print a

##
print '\n'
a = [1, 2, 3, 4, 5, 6]
print a
print a.pop() 
print a.pop()
print a.pop()
print a.pop()
print a
a.append(34)
print a

##
print '\n'
a = [1, 2, 3, 4, 5]
print a
a.append(1)
print a

##
print '\n'
a = [1, 2, 3, 4, 5]
print a
a.append(1)
print a
print a.pop(0)
print a.pop(0)
print a

## List Comprehension
print '\n'
a = [1, 2, 3]
print a
print [x ** 2 for x in a]
z = [x + 1 for x in [x ** 2 for x in a]]
print z
