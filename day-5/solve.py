# http://adventofcode.com/day/5

import re

input = open('input.txt').read()
words = input.split('\n')

def part1(words):
    # pattern to match all strings that contain:
    # at least one instance where the same letter repeats twice
    # at least 3 vowels (aeiou)
    # none of the substrings ab, cd, pq or xy
    pattern = re.compile(r'^(?=.*(\w)\1+)(?=(.*?[aeiou].*?){3,})^((?!ab|cd|pq|xy).)*$.*')

    # filter to all words that are nice
    nice = [word for word in words if pattern.search(word)]

    return len(nice)

def part2(words):
    # pattern to match all strings that contain:
    # a pair of any two letters that appear at least twice
    # at least one pair of the same letter with any other in between them
    pattern = re.compile(r'^(?=.*(\w{2}).*\1)(?=.*(\w).\2).*')

    # filter to all words that are nice
    nice = [word for word in words if pattern.search(word)]

    return len(nice)

print("Solution to part 1: %d" % part1(words))
print("Solution to part 2: %d" % part2(words))
