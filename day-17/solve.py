# http://adventofcode.com/day/17

import itertools
from pprint import pprint
from collections import Counter

eggnog = 150
containers = [43, 3, 4, 10, 21, 44, 4, 6, 47, 41, 34, 17, 17, 44, 36, 31, 46, 9, 27, 38]

def part1(eggnog, containers):
    total = 0

    # make every combination of the containers and check if the sum equals the amount of eggnog
    for i in range(len(containers)):
        for combination in itertools.combinations(containers, i):
            if sum(combination) == eggnog:
                total += 1

    return total

def part2(eggnog, containers):
    total = 0

    # make every combination of the containers and check if the sum equals the amount of eggnog
    # only return the amount of containers with the least amount of containers
    for i in range(len(containers)):
        for combination in itertools.combinations(containers, i):
            if sum(combination) == eggnog:
                total += 1

        if total > 0:
            return total

print("Solution to part 1: %s" % part1(eggnog, containers))
print("Solution to part 2: %s" % part2(eggnog, containers))
