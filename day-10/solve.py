# http://adventofcode.com/day/10

import re
import time

input = 1321131112

# method to look at a number and say the digits in it
# https://en.wikipedia.org/wiki/Look-and-say_sequence
#
# for example:
#
# input: 1211
# output: 111221 (one 1, one 2, two 1s)
def look_and_say(number):
    newNumber = ''
    # group all repeating digits    
    pattern = re.compile(r'(\d)\1*')
    groups = [match.group() for match in pattern.finditer(str(number))]

    # for every group first add the amount of the group and then the
    # digit of the group to the newNumber
    for group in groups:
        newNumber += str(len(group)) + str(group[0])

    # return the new number
    return newNumber

def part1(input):
    # execute look_and_say 40 times on the input
    for i in range(0, 40):
        input = look_and_say(input)

    # return the length of the final number
    return len(input)

def part2(input):
    # execute look_and_say 50 times on the input
    for i in range(0, 50):
        input = look_and_say(input)

    # return the length of the final number
    return len(input)


print("Input: %s" % input)
print("---")

start = time.time()
print("Solution to part 1: %s" % part1(input))
print("Duration: %s seconds" % str(time.time() - start))

start = time.time()
print("Solution to part 2: %s" % part2(input))
print("Duration: %s seconds" % str(time.time() - start))

