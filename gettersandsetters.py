class Student(object):
	def __init__(self, name):
		self.name = name


std = Student('Meet Shah')
print std.name
std.name = 'Python'
print std.name		