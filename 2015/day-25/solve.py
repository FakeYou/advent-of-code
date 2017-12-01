# http://adventofcode.com/day/25

import time

def part1(column, row):
    code = 20151125
    row = column + row - 1
    box = 1
    c = 0

    while row > 0:
        box += c
        row -= 1
        c += 1

    box += column - 1

    while box > 1:
        box -= 1
        code = code * 252533
        code = code % 33554393

    return code

start = time.time()
print("Solution to part 1: %s" % part1(row = 2947, column = 3029))
print("Duration: %s seconds" % str(time.time() - start))
