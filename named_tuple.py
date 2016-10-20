from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, y=20)
print p
print p.x + p.y
print p[0] + p[1] # Accessing the values in a normal way
x, y = p # Unpacking the tuple
print x
print y