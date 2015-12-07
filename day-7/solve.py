# http://adventofcode.com/day/7

import re
import time
from pprint import pprint

input = open('input.txt').read()
# prepend all variables with an underscore '_' to prevent collisions
input = re.sub(r'([a-z]+)', r'_\1', input)
instructions = input.split('\n')

operators = {
    'AND': '&',
    'OR': '|',
    'LSHIFT': '<<',
    'RSHIFT': '>>',
    'NOT': '~'
}

def part1(instructions):
    # loop through all instruction until all are executed.
    # every instruction is reformatted to a python correct string
    # which is then run using the 'exec' function.
    # if the 'exec' function throws an error we put the instruction back on the stack
    while len(instructions) > 0:
        # format to a string that python can execute
        instruction = instructions.pop(0)
        parts = instruction.split(' -> ')
        command = parts[1] + ' = ' + parts[0]

        # replace keywords with their operators
        for word, operator in operators.items():
            command = command.replace(word, operator)

        # try to execute the command
        try:
            exec(command)

            # make sure we wrap around back to 2^16
            if locals()[parts[1]] < 0:
                locals()[parts[1]] += 2 << 15
        except:
            # if the command did not execute properly then throw it back on the stack
            instructions.append(instruction)

    return locals()['_a']

def part2(instructions):
    # use the solution of part 1 and save it to _b
    _b = part1(instructions[:])

    # loop through all instruction until all are executed.
    # every instruction is reformatted to a python correct string
    # which is then run using the 'exec' function.
    # if the 'exec' function throws an error we put the instruction back on the stack
    while len(instructions) > 0:
        # format to a string that python can execute
        instruction = instructions.pop(0)
        parts = instruction.split(' -> ')
        command = parts[1] + ' = ' + parts[0]

        # replace keywords with their operators
        for word, operator in operators.items():
            command = command.replace(word, operator)

        # try to execute the command
        try:
            exec(command)

            # make sure we wrap around back to 2^16
            if locals()[parts[1]] < 0:
                locals()[parts[1]] += 2 << 15
        except:
            # if the command did not execute properly then throw it back on the stack
            instructions.append(instruction)

    return locals()['_a']

start = time.time()
print("Solution to part 1: %s" % part1(instructions[:]))
print("Duration: %s seconds" % str(time.time() - start))

start = time.time()
print("Solution to part 2: %s" % part2(instructions[:]))
print("Duration: %s seconds" % str(time.time() - start))
