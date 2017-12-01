# http://adventofcode.com/day/23

import time
from pprint import pprint
from operator import mul
from functools import reduce
from itertools import combinations

packages = [
    1, 3, 5, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 
    59, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113
]

def getQE(packages, groups):
    group_size = sum(packages) / groups

    for i in range(len(packages)):
        combs = [reduce(mul, c) for c in combinations(packages, i) if sum(c) == group_size]
        if combs:
            return min(combs)


def part1(packages):
    return getQE(packages, 3)

def part2(packages):
    return getQE(packages, 4)

start = time.time()
print("Solution to part 1: %s" % part1(packages))
print("Duration: %s seconds" % str(time.time() - start))

start = time.time()
print("Solution to part 2: %s" % part2(packages))
print("Duration: %s seconds" % str(time.time() - start))

