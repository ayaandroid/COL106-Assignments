class Treasure:
	
	def __init__(self, id, size, arrival_time):
		self.id = id
		self.size = size
		self.arrival_time = arrival_time
		self.completion_time = None
	
	def init_remaining_size(self):
		self.rem_size = self.size
