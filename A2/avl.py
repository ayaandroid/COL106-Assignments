from node import Node

class AVLTree:
	def __init__(self):
		self.root = Node()
		
	def search(self, key):
		v = self.root
		while v.key != None:
			if v.key == key:
				break
			elif v.key < key:
				v = v.right
			else:
				v = v.left
		return v
		
	def insert(self, key, value):
		v = self.search(key)

		if v.key != None: 
			return
			
		v.key = key
		v.value = value
		v.left = Node()
		v.left.parent = v
		v.right = Node()
		v.right.parent = v
		
		if v.parent == None:
			self.root = v

		self._rebalance(v)
		
	def _rebalance(self, v):
		while v != None:
			v.height = 1 + max(v.left.height, v.right.height)
			balance_factor = v.left.height - v.right.height
			if balance_factor == -2:
				if v.right.right.height >= v.right.left.height:
					self._L_rot(v)
				else:
					self._R_rot(v.right)
					self._L_rot(v)
			elif balance_factor == 2:
				if v.left.left.height >= v.left.right.height:
					self._R_rot(v)
				else:
					self._L_rot(v.left)
					self._R_rot(v)
			v = v.parent
	
	def _L_rot(self, v):
		if v.parent == None:    #v is root
			self.root = v.right
		else:
			if v.parent.key > v.key:    #v is left child
				v.parent.left = v.right
			else:   #v is right child
				v.parent.right = v.right
		v.right.parent = v.parent
		v.right.left.parent = v
		v.parent = v.right
		v.right = v.right.left
		v.parent.left = v
		v.height = 1 + max(v.left.height, v.right.height)
	
	def _R_rot(self, v):
		if v.parent == None:    #v is root
			self.root = v.left
		else:
			if v.parent.key > v.key:    #v is left child
				v.parent.left = v.left
			else:   #v is right child
				v.parent.right = v.left
		v.left.parent = v.parent
		v.left.right.parent = v
		v.parent = v.left
		v.left = v.left.right
		v.parent.right = v
		v.height = 1 + max(v.left.height, v.right.height)
		
	def delete(self, key):
		v = self.search(key)
		
		if v.key == None:
			return
		
		if v.left.key != None and v.right.key != None:
			s = self.successor(key)
			v.key = s.key
			v.value = s.value
			v = s
		
		if v.left.key == None and v.right.key == None:
			if v.parent == None:	#v is root
				self.root = Node()
			else:
				if v.parent.key > v.key:	#v is left child
					v.parent.left = Node()
					v.parent.left.parent = v.parent
				else:	#v is right child
					v.parent.right = Node()
					v.parent.right.parent = v.parent
			v = v.parent
		elif v.left.key == None:
			v.key = v.right.key
			v.value = v.right.value
			v.right = Node()
			v.right.parent = v
		elif v.right.key == None:
			v.key = v.left.key
			v.value = v.left.value
			v.left = Node()
			v.left.parent = v
		
		self._rebalance(v)
	
	def successor(self, key):
		v = self.root
		ans = None
		while v.key != None:
			if v.key > key:
				ans = v
				v = v.left
			else:
				v = v.right
		return ans
		
	def inorder(self, visit = lambda v: print(v.key), start = None):
		def rec(v):
			if v.key == None:
				return
			rec(v.left)
			visit(v)
			rec(v.right)
		if start == None:
		    start = self.root
		rec(start)