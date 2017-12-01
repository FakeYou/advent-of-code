# http://adventofcode.com/day/18

import time
import numpy as np
from scipy import signal
from pprint import pprint

input = open('input.txt').read()

# create a two-dimensional array of the input
# where '#' = 1 and '.' = 0
grid = np.array([list(map(lambda n: 1 if n is '#' else 0, row)) for row in input.split('\n')])

# get the next step of the grid
# following these rules:
#   A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
#   A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
def nextStep(grid):
    # create a two dimensional grid with the count of the amount of neighbours
    # that are on for each cell
    neighbours = np.ones((3, 3))
    neighbours[1][1] = 0
    counts = signal.convolve2d(grid, neighbours, mode='same', boundary='fill')   

    # create a new grid with lights turned on based on the counts and the above rules
    new = np.zeros(grid.shape)
    new[counts==3] = 1
    new[np.logical_and(counts==2, grid==1)] = 1 

    return new

def part1(grid):
    for i in range(100):
        grid = nextStep(grid)

    pprint(np.sum(grid))

def part2(grid):
    for i in range(100):
        grid = nextStep(grid)
        # set the corners to 1
        grid[::grid.shape[0]-1, ::grid.shape[1]-1] = 1

    pprint(np.sum(grid))

start = time.time()
print("Solution to part 1: %s" % part1(grid))
print("Duration: %s seconds" % str(time.time() - start))

start = time.time()
print("Solution to part 2: %s" % part2(grid))
print("Duration: %s seconds" % str(time.time() - start))
