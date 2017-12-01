# http://adventofcode.com/day/9

import re
import sys
import time
from pprint import pprint

input = open('input.txt').read()
routes = input.split('\n')

# get a dict with every location and the distance to the other locations
# for example:
#
# input:
#   London to Dublin = 464
#   London to Belfast = 518
#   Dublin to Belfast = 141
#
# output:
#   { "London": { "Dublin": 464, "Belfast": 518 },
#     "Dublin": { "London": 464, "Belfast": 141 },
#     "Belfast": { "London": 518, "Dublin": 141 } }
def getGraph(routes):
    graph = {}
    for route in routes:
        # extra locations and distance from text
        (start, end, distance) = re.search(r'^(\w+) to (\w+) = (\d+)$', route).groups()

        # make sure the locations exists in the graph
        if not start in graph:
            graph[start] = {}
        if not end in graph:
            graph[end] = {}

        # save the distance between the locations for both locations
        graph[start][end] = int(distance) 
        graph[end][start] = int(distance) 

    return graph

# get a two dimensional array with all the permutations in order for an array
# for example:
#
# input: [1, 2, 3]
#
# output:
#     [[1, 2, 3],
#      [1, 3, 1],
#      [2, 1, 3],
#      [2, 3, 1],
#      [3, 1, 2],
#      [3, 2, 1]]
def getPermutations(array):
    results = []

    # recursive method
    def permute(array, memo=[]):
        for i in range(0, len(array)):
            current = array[i:i+1]
            array.pop(i)

            if len(array) is 0:
                results.append(current + memo)

            permute(array[:], current + memo)

            array.insert(i, current[0])

        return results

    return permute(array)

# get the distance of every permutation of a graph 
def getGraphDistances(graph):
    distances = []
    permutations = getPermutations(list(graph))

    # loop through every permutation and calculate the total distance
    for permutation in permutations:
        distance = 0

        # add the distance between every person
        for i in range(0, len(permutation) - 1):
            (start, end) = permutation[i:i + 2]

            distance += graph[start][end]

        distances.append(distance)

    return distances


def part1(routes):
    graph = getGraph(routes)

    distances = getGraphDistances(graph)
    distances.sort()

    return distances[0]

def part2(routes):
    graph = getGraph(routes)

    distances = getGraphDistances(graph)
    distances.sort()

    return distances[-1]

start = time.time()
print("Solution to part 1: %s" % part1(routes))
print("Duration: %s seconds" % str(time.time() - start))

start = time.time()
print("Solution to part 2: %s" % part2(routes))
print("Duration: %s seconds" % str(time.time() - start))