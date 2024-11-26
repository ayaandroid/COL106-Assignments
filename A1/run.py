from maze import *
from navigator import *

def test(grid, start, end):

    m, n = len(grid), len(grid[0])
    maze = Maze(m, n)
    for i in range(m): 
        for j in range(n): 
            if grid[i][j] == 1: maze.add_ghost(i,j)
    print('Maze')
    maze.print_grid()
    print('-'*70)

    PacManInstance = PacMan(maze)
    path = PacManInstance.find_path(start, end)
    for cell in path: grid[cell[0]][cell[1]] = '*'
    print('Path found successfully')
    for row in grid:
        for cell in row: print(cell, end = '')
        print()
    print('-'*70)

grid = [
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 0]
]

start = (2, 0)
end = (2, 3)

test(grid, start, end)
