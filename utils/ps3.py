import pandas as pd
import numpy as np
EMPTY, WALL, TARGET, USED = ".","X","T","o"
c  = pd.Series({"EMPTY": ".", "WALL":"X", "TARGET":"T", "USED":"o"})
ci = pd.Series({".": 0, "X": 255, "T":100, "o":200})


def possible_moves(grid, y,x):
    moves = [ [y,x+1], [y-1,x], [y,x-1], [y+1,x]]
    
    moves = [(my,mx) for my,mx in moves if mx>=0 and mx<len(grid[0]) and \
                                           my>=0 and my<len(grid) and grid[my][mx]!=c.WALL]    
    return moves

def cost_search(grid):
    start = (0,0)
    step_cost = 1
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from   = {}
    cost_so_far = {}
    came_from[start]   = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        y,x = current
        if grid[y][x] == c.TARGET:
            break
        
        for next in possible_moves(grid,y,x):
            new_cost = cost_so_far[current] + step_cost
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current
                                
    return came_from, cost_so_far



