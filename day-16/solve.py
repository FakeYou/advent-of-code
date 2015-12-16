# http://adventofcode.com/day/15

import re
import time
from pprint import pprint

input = open('input.txt').read()
 
# extract all the compounds of each aunt
pattern = re.compile(r'^.*?(\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)$', re.MULTILINE)

aunts = [list(m.groups()) for m in pattern.finditer(input)]

MFCSAM = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

def part1(aunts):
    for aunt in aunts:
        compounds = aunt[1:]

        # check if each compound equals the definition as given by the MFCSAM
        for i in range(0, len(compounds), 2):
            if MFCSAM[compounds[i]] != int(compounds[i + 1]):
                break
        else:
            # if the above loop didn't break than we found our aunt
            return aunt[0] 

def part2(aunts):
    for aunt in aunts:
        compounds = aunt[1:]

        # check if each compound equals the definition as given by the MFCSAM
        for i in range(0, len(compounds), 2):
            definition = int(MFCSAM[compounds[i]])
            value = int(compounds[i + 1])

            # the compounds 'cats' and 'trees' are 'greater than'
            if compounds[i] in ['cats', 'trees']:
                if value <= definition:
                    break
            # the compounds 'pomeranians' and 'goldfish' are 'less than'
            elif compounds[i] in ['pomeranians', 'goldfish']:
                if value >= definition: 
                    break
            # the other compounds are 'equals'
            elif value != definition:
                break
        else:
            return aunt[0]

start = time.time()
print("Solution to part 1: %s" % part1(aunts))
print("Duration: %s seconds" % str(time.time() - start))

start = time.time()
print("Solution to part 2: %s" % part2(aunts))
print("Duration: %s seconds" % str(time.time() - start))

