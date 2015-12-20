# http://adventofcode.com/day/20

import time
from pprint import pprint
from collections import Counter, defaultdict

threshold = 36000000

def part1(threshold):
    houses = Counter()
    for elf in range(1, round(threshold/10)):
        for house in range(elf, round(threshold/10), elf):
            houses[house] += elf * 10

            if houses[elf] >= threshold:
                return house

def part2(threshold):
    houses = Counter()

    for elf in range(1, round(threshold/10)):
        for house in range(elf, elf * 50 + 1, elf):
            houses[house] += elf * 11

            if houses[elf] >= threshold:
                return house

start = time.time()
print("Solution to part 1: %s" % part1(threshold))
print("Duration: %s seconds" % str(time.time() - start))

start = time.time()
print("Solution to part 2: %s" % part2(threshold))
print("Duration: %s seconds" % str(time.time() - start))
