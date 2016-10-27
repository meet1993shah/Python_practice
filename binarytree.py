class Node(object):
	def __init__(self, val):
		self.val = val
		self.lchild = None
		self.rchild = None

	def insert(self, data):
		if self.val == data:
			return False
		elif data < self.val:
			if self.lchild:
				return self.lchild.insert(data)
			else:
				self.lchild = Node(data)
				return True
		else:
			if self.rchild:
				return self.rchild.insert(data)
			else:
				self.rchild = Node(data)
				return True

	def find(self, data):
		if	self.val == data:
			return True
		elif data < self.val:
			if self.lchild:
				return self.lchild.find(data)
			else:
				return False
		else:
			if self.rchild:
				return self.rchild.find(data)
			else:
				return False

	def preorder(self):
		if self:
			print self.val
			if self.lchild:
				self.lchild.preorder()
			if self.rchild:
				self.rchild.preorder()

	def postorder(self):
		if self:
			if self.lchild:
				self.lchild.postorder()
			if self.rchild:
				self.rchild.postorder()
			print self.val	

	def inorder(self):
		if self:
			if self.lchild:
				self.lchild.inorder()
			print self.val	
			if self.rchild:
				self.rchild.inorder()									



class BinaryTree(object):
	def __init__(self):
		self.root = None

	def insert(self, data):
		if self.root:
			return self.root.insert(data)
		else:
			self.root = Node(data)
			return True

	def find(self, data):
		if self.root:
			return self.root.find(data)
		else:
			return False

	def preorder(self):
		print "Preorder"
		self.root.preorder()

	def postorder(self):
		print "Postorder"
		self.root.postorder()

	def inorder(self):
		print "Inorder"
		self.root.inorder()				

b = BinaryTree()
b.insert(15)
b.insert(8)
b.insert(24)
b.insert(5)
b.insert(30)
b.insert(19)
b.insert(21)
print b.preorder()
print b.postorder()
print b.inorder()




