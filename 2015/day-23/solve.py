# http://adventofcode.com/day/23

import time
from pprint import pprint

input = open('input.txt').read()

registers = {
    'a': 0,
    'b': 0
}

instructions = input.split('\n')

def execute(instructions, registers):
    line_number = 0

    while line_number < len(instructions):
        line = instructions[line_number]

        instruction = line[:3]
        arguments = line[4:].replace(' ', '').split(',')

        if instruction == 'hlf':
            registers[arguments[0]] = int(registers[arguments[0]] / 2)
            line_number += 1

        if instruction == 'tpl':
            registers[arguments[0]] *= 3
            line_number += 1
        
        if instruction == 'inc':
            registers[arguments[0]] += 1
            line_number += 1
        
        if instruction == 'jmp':
            line_number += int(arguments[0])
        
        if instruction == 'jie':
            if registers[arguments[0]] % 2 == 0:
                line_number += int(arguments[1])
            else:
                line_number += 1

        if instruction == 'jio':
            if registers[arguments[0]] == 1:
                line_number += int(arguments[1])
            else:
                line_number += 1

    return registers

def part1(instructions):
    registers = { 'a': 0, 'b': 0 }
    registers = execute(instructions, registers)

    return registers['b']

def part2(instructions):
    registers = { 'a': 1, 'b': 0 }
    registers = execute(instructions, registers)

    return registers['b']

start = time.time()
print("Solution to part 1: %s" % part1(instructions))
print("Duration: %s seconds" % str(time.time() - start))

start = time.time()
print("Solution to part 2: %s" % part2(instructions))
print("Duration: %s seconds" % str(time.time() - start))
