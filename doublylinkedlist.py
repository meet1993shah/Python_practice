class Node(object):
	def __init__(self,dat,prv,nxt):
		self.dat = dat
		self.prv = prv
		self.nxt = nxt

class DoubleList(object):
	head = None
	tail = None

	def show(self):
		print "Printing the linked-list data"
		current_node = self.head
		while current_node is not None:
			print current_node.dat, "<->",
			current_node = current_node.nxt
		print None

	def append(self, dat):
		new_node = Node(dat, None, None)
		if self.head is None:
			self.head = self.tail = new_node
		else:
			new_node.prv = self.tail
			new_node.nxt = None
			self.tail.nxt = new_node
		self.tail = new_node

	def remove(self, node_val):
		current_node = self.head
		while current_node is not None:
			if current_node.dat == node_val:
				if current_node.prv is not None:
					current_node.prv.nxt = current_node.nxt
					current_node.nxt.prv = current_node.prv
				else:
					self.head = current_node.nxt
					current_node.nxt.prv = None
			current_node = current_node.nxt

if __name__ == '__main__':
	d = DoubleList()
	d.append(5)
	d.append(6)
	d.append(50)
	d.append(30)
	d.show()
	d.remove(50)
	d.remove(5)
	d.show()

