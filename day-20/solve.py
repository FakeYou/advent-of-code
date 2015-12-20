# http://adventofcode.com/day/20

import time
from pprint import pprint
from collections import Counter

threshold = 36000000

def part1(threshold):
    houses = Counter()
    for elf in range(1, round(threshold/10)):
        for house in range(elf, round(threshold/10), elf):
            houses[house] += elf * 10

        print(elf)

    for house, presents in houses.items():
        if presents == threshold:
            return house

print(["--", part1(threshold)])
