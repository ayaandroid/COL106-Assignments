from maze import *
from exception import *
from stack import *

class PacMan:

	def __init__(self, grid):
		self.navigator_maze = grid.grid_representation
		
	def find_path(self, start, end):
		if self.navigator_maze[start[0]][start[1]] == 1 or self.navigator_maze[end[0]][end[1]] == 1:
			raise PathNotFoundException
			
		m = len(self.navigator_maze)
		n = len(self.navigator_maze[0])
		
		visited = [[False]*n for i in range(m)]
		
		path = Stack()
		path.push(start)
		
		while not path.is_empty():
			current = path.top()
			visited[current[0]][current[1]] = True
			
			if current == end:
				return path.data
				
			if current[0]+1 < m and not visited[current[0]+1][current[1]] and self.navigator_maze[current[0]+1][current[1]] != 1:
				path.push((current[0]+1, current[1]))
			elif current[0]-1 >= 0 and not visited[current[0]-1][current[1]] and self.navigator_maze[current[0]-1][current[1]] != 1:
				path.push((current[0]-1, current[1]))
			elif current[1]+1 < n and not visited[current[0]][current[1]+1] and self.navigator_maze[current[0]][current[1]+1] != 1:
				path.push((current[0], current[1]+1))
			elif current[1]-1 >= 0 and not visited[current[0]][current[1]-1] and self.navigator_maze[current[0]][current[1]-1] != 1: 
				path.push((current[0], current[1]-1))
			else:
				path.pop()
			
		raise PathNotFoundException
