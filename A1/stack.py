from copy import deepcopy

class Stack:
	
	def __init__(self, max_size):
		self.__L = [None]*max_size
		self.__top = -1
		self.__cap = max_size

	def is_empty(self):
		return self.__top == -1
	
	class StackOverFlowException(Exception):
		def __init__(self):
			super().__init__("Stack is full")
	
	def push(self, e):
		if self.__top == self.__cap - 1:
			raise StackOverflowException
		self.__top += 1
		self.__L[self.__top] = e
		
	class EmptyStackException(Exception):
		def __init__(self):
			super().__init__("Stack is empty")

	def pop(self):
		if self.is_empty():
			raise EmptyStackException
		self.__L[self.__top] = None
		self.__top -= 1
		
	def get_top(self):
		if self.is_empty():
			raise EmptyStackException
		return deepcopy(self.__L[self.__top])
	
	def get_L(self):
		return deepcopy(self.__L[:self.__top+1])
