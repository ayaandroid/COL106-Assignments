class Stack:
	
	def __init__(self): self.data = []

	def is_empty(self): return len(self.data) == 0
	
	def push(self, e): self.data.append(e)

	def pop(self):
		if self.is_empty(): raise Exception('Stack is empty')
		return self.data.pop()
		
	def top(self):
		if self.is_empty(): raise Exception('Stack is empty')
		return self.data[-1]
