# http://adventofcode.com/day/3

from pprint import pprint

input = open('input.txt').read()

directions = {
    '^': { 'x': 0, 'y': -1 },   # north
    '>': { 'x': 1, 'y': 0 },    # east
    'v': { 'x': 0, 'y': 1 },    # south
    '<': { 'x': -1, 'y': 0 }    # west
}

size = 250

def part1(input):
    # create a grid of (size)x(size)
    grid = [[0 for x in range(size)] for x in range(size)] 

    # start in the middle of the grid
    (x, y) = [int(size/2), int(size/2)]

    # give a present at the start
    grid[y][x] += 1

    for dir in list(input):
        # move on the x and y axis according to the direction
        x += directions[dir]['x']
        y += directions[dir]['y']

        # give a present at the new location
        grid[y][x] += 1


    # flatten grid to a list of all houses
    houses = [house for row in grid for house in row]
    # filter to only the houses with 1 or more visits
    visited = [n for n in houses if n >= 1]

    # return the amount of visited houses
    return len(visited)

def part2(input):
    # create a grid of (size)x(size)
    grid = [[0 for x in range(size)] for x in range(size)] 

    # start santa and robotsanta in the middle of the grid
    santa = { "x": int(size/2), "y": int(size/2) }
    robot = { "x": int(size/2), "y": int(size/2) }

    # give a present at the start
    grid[santa["y"]][santa["x"]] += 1

    for index, dir in enumerate(list(input)):
        # select which agent should move, 
        # santa moves on the even turns, robotsanta moves on the odd turns
        agent = santa if index % 2 is 0 else robot

        # move on the x and y axis according to the direction
        agent["x"] += directions[dir]['x']
        agent["y"] += directions[dir]['y']

        # give a present at the new location
        grid[agent["y"]][agent["x"]] += 1


    # flatten grid to a list of all houses
    houses = [house for row in grid for house in row]
    # filter to only the houses with 1 or more visits
    visited = [n for n in houses if n >= 1]

    # return the amount of visited houses
    return len(visited)


print("Solution to part 1: %d" % part1(input))
print("Solution to part 2: %d" % part2(input))