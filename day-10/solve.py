# http://adventofcode.com/day/10

import re
import time

input = 1321131112

def look_and_say(number):
    newNumber = ''
    pattern = re.compile(r'(\d)\1*')
    groups = [match.group() for match in pattern.finditer(str(number))]

    for group in groups:
        newNumber += str(len(group)) + str(group[0])

    return newNumber

def part1(input):
    for i in range(0, 40):
        input = look_and_say(input)

    return len(input)

def part2(input):
    for i in range(0, 50):
        input = look_and_say(input)

    return len(input)


print("Input: %s" % input)
print("---")

start = time.time()
print("Solution to part 1: %s" % part1(input))
print("Duration: %s seconds" % str(time.time() - start))

start = time.time()
print("Solution to part 2: %s" % part2(input))
print("Duration: %s seconds" % str(time.time() - start))

