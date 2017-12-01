# http://adventofcode.com/day/18

import time
import re
from pprint import pprint
from collections import Counter

input = open('input.txt').read()
electron = 'e'
medicine = 'CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl'

pattern = re.compile(r'^(\w+) => (\w+)$', re.MULTILINE)
replacements = [list(m.groups()) for m in pattern.finditer(input)]

def part1(medicine, replacements):
    molecules = []

    for replacement in replacements:
        indices = []

        # find all indices of the replacement key in the medicin
        indices = [m.start() for m in re.finditer(replacement[0], medicine)]
        # replace every occurence of the key with the value 
        # and add it to the total list of molecules
        for index in indices:
            molecules.append(medicine[:index] + replacement[1] + medicine[index + len(replacement[0]):])

    # return the amount of unique molecules
    return len(Counter(molecules).keys())

def part2(electron, medicine, replacements):
    molecules = [electron]
    target = medicine
    steps = 0

    # start with the medicine and work backwards
    while target != electron:
        # replace every value of a replacement with its key
        for replacement in replacements:
            if replacement[1] not in target:
                continue

            target = target.replace(replacement[1], replacement[0], 1)
            steps += 1

    return steps

start = time.time()
print("Solution to part 1: %s" % part1(medicine, replacements))
print("Duration: %s seconds" % str(time.time() - start))

start = time.time()
print("Solution to part 2: %s" % part2(electron, medicine, replacements))
print("Duration: %s seconds" % str(time.time() - start))
