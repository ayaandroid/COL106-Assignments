from bin import Bin
from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException

class GCMS:
	def __init__(self):
		self.bins = AVLTree()
		self.objects = AVLTree()
		self.bins_by_capacity = AVLTree()
		
	def add_bin(self, bin_id, capacity):
		new = Bin(bin_id, capacity)
		self.bins.insert(bin_id, new)
		self.bins_by_capacity.insert((capacity, bin_id), new)
	
	def add_object(self, object_id, size, color):
		if color == Color.BLUE:
			bin = self._compactFitLeastId(size)
		elif color == Color.YELLOW:
			bin = self._compactFitGreatestId(size)
		elif color == Color.RED:
			bin = self._largestFitLeastId(size)
		elif color == Color.GREEN:
			bin = self._largestFitGreatestId(size)
			
		if bin != None:
			new = Object(object_id, size, color)
			self.objects.insert(object_id, new)
			bin = bin.value
			new.bin = bin
			bin.add_object(new)
			self.bins_by_capacity.delete((bin.capacity, bin.bin_id))
			bin.capacity -= size
			self.bins_by_capacity.insert((bin.capacity, bin.bin_id), bin)
		else:
			raise NoBinFoundException
	
	def delete_object(self, object_id):
		obj = self.objects.search(object_id).value
		if obj != None:
			self.objects.delete(object_id)
			bin = obj.bin
			bin.remove_object(object_id)
			self.bins_by_capacity.delete((bin.capacity, bin.bin_id))
			bin.capacity += obj.size
			self.bins_by_capacity.insert((bin.capacity, bin.bin_id), bin)
			
	def bin_info(self, bin_id):
		bin = self.bins.search(bin_id).value
		if bin != None:
			obj_ids = []
			bin.objects.inorder(lambda v: obj_ids.append(v.key))
			return bin.capacity, obj_ids
	
	def object_info(self, object_id):
		obj = self.objects.search(object_id).value
		if obj != None:
			return obj.bin.bin_id
	
	def _compactFitLeastId(self, object_size):
		v = self.bins_by_capacity.root
		ans = None
		while v.key != None:
			if v.key[0] < object_size:
				v = v.right
			else:
				ans = v
				v = v.left
		return ans
	
	def _largestFitGreatestId(self, object_size):
		v = self.bins_by_capacity.root
		while v.key != None:
			v = v.right
		v = v.parent
		if v != None and v.key[0] >= object_size:
			return v
			
	def _compactFitGreatestId(self, object_size):
		x = self._compactFitLeastId(object_size)
		if x != None:
			v = self.bins_by_capacity.root
			ans = None
			while v.key != None:
				if v.key[0] > x.key[0]:
					v = v.left
				else:
					ans = v
					v = v.right
			return ans
					
	def _largestFitLeastId(self, object_size):
		x = self._largestFitGreatestId(object_size)
		if x != None:
			v = self.bins_by_capacity.root
			ans = None
			while v.key != None:
				if v.key[0] < x.key[0]:
					v = v.right
				else:
					ans = v
					v = v.left
			return ans
