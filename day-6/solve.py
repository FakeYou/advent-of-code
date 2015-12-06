# http://adventofcode.com/day/6

import re
import time

input = open('input.txt').read()
instructions = input.split('\n')

def split_coords(coords):
    return list(map(int, coords.split(',')))

def part1(instructions):
    # create a grid of 1000x1000
    grid = [[0 for x in range(1000)] for x in range(1000)] 
    
    pattern = re.compile(r'(\d{1,3},\d{1,3}) through (\d{1,3},\d{1,3})$')

    for instruction in instructions:
        (start, end) = map(split_coords, pattern.search(instruction).groups())
        # when instructions starts with 'turn on'
        # then turn every light within the coords on
        if instruction.startswith("turn on"):
            for y in range(start[1], end[1] + 1):
                for x in range(start[0], end[0] + 1):
                    grid[y][x] = 1

        # when instructions starts with 'turn off'
        # then turn every light within the coords off
        if instruction.startswith("turn off"):
            for y in range(start[1], end[1] + 1):
                for x in range(start[0], end[0] + 1):
                    grid[y][x] = 0

        # when instructions starts with 'toggle'
        # then switch every light within the coords to the other position
        if instruction.startswith("toggle"):
            for y in range(start[1], end[1] + 1):
                for x in range(start[0], end[0] + 1):
                    # change light to the other position
                    grid[y][x] = 0 if grid[y][x] is 1 else 1

    # flatten grid to a list of all houses
    lights = [light for row in grid for light in row]
    # filter to only the houses with 1 or more visits
    lit_lights = [n for n in lights if n == 1]

    return len(lit_lights)

def part2(instructions):
    # create a grid of 1000x1000
    grid = [[0 for x in range(1000)] for x in range(1000)] 
    
    pattern = re.compile(r'(\d{1,3},\d{1,3}) through (\d{1,3},\d{1,3})$')

    for instruction in instructions:
        (start, end) = map(split_coords, pattern.search(instruction).groups())
        # when instructions starts with 'turn on'
        # then increase the brightness of every light within the coords by 1
        if instruction.startswith("turn on"):
            for y in range(start[1], end[1] + 1):
                for x in range(start[0], end[0] + 1):
                    grid[y][x] += 1

        # when instructions starts with 'turn off'
        # then decrease the brightness of every light within the coords by 1
        if instruction.startswith("turn off"):
            for y in range(start[1], end[1] + 1):
                for x in range(start[0], end[0] + 1):
                    # decrease the brightness by 1 if the light has a brightness of atleast 1
                    grid[y][x] -= 1 if grid[y][x] > 0 else 0
                    if(grid[y][x] < 0):
                        print(grid[y][x])

        # when instructions starts with 'toggle'
        # then increase the brightness of every light within the coords by 2
        if instruction.startswith("toggle"):
            for y in range(start[1], end[1] + 1):
                for x in range(start[0], end[0] + 1):
                    grid[y][x] += 2

    # flatten grid to a list of all houses
    lights = [light for row in grid for light in row]

    return sum(lights)

start = time.time()
print("Solution to part 1: %s" % part1(instructions))
print("Duration: %s seconds" % str(time.time() - start))

start = time.time()
print("Solution to part 2: %s" % part2(instructions))
print("Duration: %s seconds" % str(time.time() - start))