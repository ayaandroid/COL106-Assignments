class Heap:
	def __init__(self, comparison_function, init_array):
		self._comp = comparison_function
		self._data = init_array
		self._heapify()
		
	def insert(self, value):
		self._data.append(value)
		self._upheap(len(self) - 1)
		
	def extract(self):
		if self.is_empty():
			return
			
		top = self._data[0]
		self._data[0] = self._data[-1]
		self._data.pop()
		self._downheap(0)
		return top
			
	def top(self):
		if self.is_empty():
			return
			
		return self._data[0]
    
	def _upheap(self, i):
		if i == 0:
			return
		parent = (i-1)//2
		if self._comp(self._data[i], self._data[parent]):
			self._data[i], self._data[parent] = self._data[parent], self._data[i]
			self._upheap(parent)
	
	def _downheap(self, i):
		left = 2*i + 1
		if left >= len(self):
			return
		smaller = left
		right = 2*i + 2
		if right < len(self) and self._comp(self._data[right], self._data[left]):
			smaller = right
		if self._comp(self._data[smaller], self._data[i]):
			self._data[smaller], self._data[i] = self._data[i], self._data[smaller]
			self._downheap(smaller)
			
	def _heapify(self):
		k = (len(self)-2)//2
		for i in range(k, -1, -1):
			self._downheap(i)
			
	def is_empty(self):
		return len(self) == 0
	
	def __iter__(self):
		return iter(self._data)
	
	def __len__(self):
		return len(self._data)
