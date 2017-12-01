# http://adventofcode.com/day/8

import re
from enum import Enum

input = open('input.txt').read()
strings = input.split('\n')

class State(Enum):
    none = 1
    char = 2
    escape = 3
    hex1 = 4
    hex2 = 5

def part1(strings):
    totalCodeBytes = 0
    totalStringBytes = 0

    for string in strings:
        state = State.none

        codeBytes = 0;
        stringBytes = 0;

        # loop through every character in the string and process it based on the state
        for char in string:
            codeBytes += 1

            # state is none for the first character and when a closing '"' is found
            if state == State.none:
                state = State.char
                continue

            # normal character are counted as string bytes unless it is a '"' or '\'
            if state == State.char:
                if char == '"':
                    state = State.none
                elif char == '\\':
                    state = State.escape
                else:                
                    stringBytes += 1
                continue

            # when the state is 'escape'
            if state == State.escape:
                # if the escape starts with an 'x' then we have a hex character of two extra bytes
                # for example \x27 = "'"
                if char == 'x':
                    state = State.hex1
                else:
                    state = State.char
                    stringBytes += 1
                continue

            # move from the first hex character to the second
            if state == State.hex1:
                state = State.hex2
                continue

            # close the hex character and save as 1 string byte
            if state == State.hex2:
                state = State.char
                stringBytes += 1
                continue

        totalCodeBytes += codeBytes
        totalStringBytes += stringBytes

    # return the difference between the amount of code bytes and string bytes
    return totalCodeBytes - totalStringBytes

def part2(strings):
    encodedStrings = []

    for string in strings:
        encodedString = ''

        # encode special characters and save to new string
        for char in string:
            # encode '"' to '\"'
            if char == '"':
                encodedString += '\\"'
            # encode '\' to '\\'
            elif char == '\\':
                encodedString += '\\\\'
            else:
                encodedString += char

        # surround encoded string with quotes '"'
        encodedStrings.append('"' + encodedString + '"')

    # use solution of part 1 to count the difference between code and string bytes
    return part1(encodedStrings)

print("Solution to part 1: %d" % part1(strings))
print("Solution to part 2: %d" % part2(strings))
