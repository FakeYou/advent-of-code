# http://adventofcode.com/day/11

import re
import time

input = b'hxbxwxba'

# increment a string as if the characters were numbers
#
# for example:
#
# input: abcdefgh
# output: abcdefgi
def increment_string(string):
    incremented_string = []
    carry_over = True

    # loop through all bytes of the string in reverse order
    # increment the char if it's a carry over 
    # if the char is more then 122 (1 past 'z') then we loop
    # back to 'a' and set the carry over flag
    for char in string[::-1]:
        if carry_over:
            carry_over = False
            char += 1

        if char > 122:
            carry_over = True
            char = 97

        incremented_string.append(char)

    # reverse the incremented string back again and return it
    return bytes(incremented_string[::-1])

# check if the a password is valid
# a password is valid if:
# - it doesn't contain the letters i, o, or l
# - it contains at least two different, non-overlapping pairs of letters
# - it include one increasing straight of at least three letters
def valid_password(password):
    similar_char_pattern = re.compile(r'^[iol]*$')
    two_pairs_pattern = re.compile(r'(?:.*(\w)\1){2}')

    # return false it it contains the letters i, o or l
    if similar_char_pattern.match(str(password)):
        return False

    # return false if it doesn't contain two pairs of letters
    if not two_pairs_pattern.match(str(password)):
        return False

    # return true if it contains an increasing straight of at least three letters
    for i in range(0, len(password) - 2):
        if password[i] == password[i + 1] - 1 and \
           password[i] == password[i + 2] - 2:
            return True

    return False

def part1(password):
    # find the first valid password by incrementing it
    while not valid_password(password):
        password = increment_string(password)

    return password

def part2(password):
    # use part1 to find the first valid password after the initial input
    # increment this result and find the second valid password
    return part1(increment_string(part1(password)))
    
print("Input: %s" % input)
print("---")

start = time.time()
print("Solution to part 1: %s" % part1(input))
print("Duration: %s seconds" % str(time.time() - start))

start = time.time()
print("Solution to part 2: %s" % part2(input))
print("Duration: %s seconds" % str(time.time() - start))

