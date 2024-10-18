from avl import AVLTree
from object import Object, Color
class Bin:
	def __init__(self, bin_id, capacity):
		self.bin_id = bin_id
		self.capacity = capacity
		self.objects = AVLTree()
		
	def add_object(self, object):
		self.objects.insert(object.object_id, object)
	
	def remove_object(self, object_id):
		self.objects.delete(object_id)
