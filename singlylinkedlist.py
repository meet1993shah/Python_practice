class Node(object):

	def __init__(self, dat, nxt):
		self.dat = dat
		self.nxt = nxt

class SingleList(object):
	
	def __init__(self):
		self.head = None
		self.tail = None

	def show(self):
		print "Printing the linked-list data"
		current_node = self.head
		while current_node is not None:
			print current_node.dat, "->",
			current_node = current_node.nxt
		print None

	def append(self, dat):
		node = Node(dat, None)
		if self.head is None:
			self.head = self.tail = node
		else:
			self.tail.nxt = node
		self.tail = node
	
	def remove(self, node_val):
		current_node = self.head
		previous_node = None
		while current_node is not None:
			if current_node.dat == node_val:
				if previous_node.nxt is not None:
					previous_node.nxt = current_node.nxt
				else:
					self.head = current_node.nxt
			previous_node = current_node
			current_node = current_node.nxt

if __name__ == '__main__':
	s = SingleList()
	s.append(31)
	s.append(2)
	s.append(10)
	s.append(3)
	s.show()

	s.remove(10)
	s.show()



