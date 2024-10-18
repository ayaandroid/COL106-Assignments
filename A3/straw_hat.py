from crewmate import CrewMate
from heap import Heap
from treasure import Treasure
from custom import comp1, comp2

class StrawHatTreasury:
	def __init__(self, m):
		self.crewmates = Heap(comp1, [CrewMate(i) for i in range(m)])
		self.active_crewmates = []
        
	def add_treasure(self, treasure):
		least_load = self.crewmates.extract()
		least_load.chests.append(treasure)
		if least_load.completion_time == 0:
			self.active_crewmates.append(least_load)
		least_load.completion_time = max(least_load.completion_time, treasure.arrival_time) + treasure.size
		self.crewmates.insert(least_load)
    
	def get_completion_time(self):
		
		result = []
		
		for crewmate in self.active_crewmates:
			
			processing_queue = Heap(comp2, [])
			
			for x in crewmate.chests:
				
				while not processing_queue.is_empty():
					
					y = processing_queue.top()
					if y.rem_size <= x.arrival_time - t:
						t += y.rem_size
						y.completion_time = t
						result.append(y)
						processing_queue.extract()
					else:
						y.rem_size -= x.arrival_time - t
						break
						
				x.init_remaining_size()
				processing_queue.insert(x)
				t = x.arrival_time
				
			while not processing_queue.is_empty():
				y = processing_queue.extract()
				t += y.rem_size
				y.completion_time = t
				result.append(y)
				
		result.sort(key = lambda T: T.id)
		return result
