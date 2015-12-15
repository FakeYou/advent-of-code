# http://adventofcode.com/day/15

import re
import time
import operator
from functools import reduce
from pprint import pprint

input = open('input.txt').read()
 
# extract the values of the different properties of an ingredient as a two dimensional array of ints
pattern = re.compile(('^.*?'
                      '([\-0-9]+)' '.*?'
                      '([\-0-9]+)' '.*?'
                      '([\-0-9]+)' '.*?'
                      '([\-0-9]+)' '.*?'
                      '([\-0-9]+)$'), re.MULTILINE)
ingredients = [list(map(int, m.groups())) for m in pattern.finditer(input)]

# method to get the product of the factors
def prod(factors):
    return reduce(operator.mul, factors, 1)

# caclulate the score based on the ingredient values and the ratio of each ingredient
def calculateScore(ingredients, ratio):
    rotate = [list(l) for l in list(zip(*ingredients))]

    # black magic
    return prod([max(0, sum(map(lambda pair: prod(pair), zip(rot, ratio)))) for rot in rotate])

# calculate the highest-scoring ingredient ratio for the best cookie
def part1(ingredients):
    maxScore = 0

    # remove the calorie value for each ingredient
    ingredients = [ingredient[:-1] for ingredient in ingredients]

    for i in range(0, 100):
        for j in range(0, 100 - i):
            for k in range(0, 100 - i - j):
                h = 100 - i - j - k

                # save the highest score
                maxScore = max(maxScore, calculateScore(ingredients, [i, j, k, h]))

    return maxScore

# calculate the highest-scoring ingredient ratio for the best cookie with exactly 500 calories
def part2(ingredients):
    maxScore = 0

    # save the calories in a seperate array
    calories = [ingredient[-1:] for ingredient in ingredients]
    ingredients = [ingredient[:-1] for ingredient in ingredients]

    for i in range(0, 100):
        for j in range(0, 100 - i):
            for k in range(0, 100 - i - j):
                h = 100 - i - j - k

                # only cookies with 500 calories are allowed
                if calculateScore(calories, [i, j, k, h]) != 500:
                    continue

                # save the highest score
                maxScore = max(maxScore, calculateScore(ingredients, [i, j, k, h]))

    return maxScore

start = time.time()
print("Solution to part 1: %s" % part1(ingredients))
print("Duration: %s seconds" % str(time.time() - start))

start = time.time()
print("Solution to part 2: %s" % part2(ingredients))
print("Duration: %s seconds" % str(time.time() - start))
