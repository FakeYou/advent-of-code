# http://adventofcode.com/day/11

import json
import time

input = open('input.txt').read()
data = json.loads(input)

# return the sum of all ints in a nested json structure
def part1(data):
    # recursive function to count the total of each element
    def reduce(data):
        total = 0
        for val in data:
            # if `int` then just add it to the total
            if isinstance(val, int):
                total += val
            # if `dict` then run only the values through the function again
            elif isinstance(val, dict):
                total += reduce(val.values())
            # if `list` then run it through the function again
            elif isinstance(val, list):
                total += reduce(val)

        return total 

    return reduce(data)

# return the sum of all ints in a nested json structure
# excluding any dicts that contain the value "red"
def part2(data):
    # recursive function to count the total of each element
    def reduce(data):
        total = 0
        for val in data:
            # if `int` then just add it to the total
            if isinstance(val, int):
                total += val
            # if `dict` then run only the values through the function again
            elif isinstance(val, dict):
                # only reduce this dict if it doesn't contain a value "red"
                if "red" not in val.values():
                    total += reduce(val.values())
            # if `list` then run it through the function again
            elif isinstance(val, list):
                total += reduce(val)

        return total 

    return reduce(data)

start = time.time()
print("Solution to part 1: %s" % part1(data))
print("Duration: %s seconds" % str(time.time() - start))

start = time.time()
print("Solution to part 2: %s" % part2(data))
print("Duration: %s seconds" % str(time.time() - start))
