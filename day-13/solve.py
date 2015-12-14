# http://adventofcode.com/day/9

import re
import sys
import time
from pprint import pprint

input = open('input.txt').read()
relations = input.split('\n')

# get a dict with every person and the happiness units compared to the other persons
# for example:
#
# input:
# Alice would gain 54 happiness units by sitting next to Bob.
# Alice would lose 2 happiness units by sitting next to David.
# Bob would gain 83 happiness units by sitting next to Alice.
# Bob would lose 63 happiness units by sitting next to David.
# David would gain 46 happiness units by sitting next to Alice.
# David would lose 7 happiness units by sitting next to Bob.
#
# output:
#   { "Alice": { "Bob": 54, David": -2 },
#     "Bob": { "Alice": 83, "David": -63 },
#     "David": { "Alice": 46, "Bob": -7 } }
def getGraph(relations):
    graph = {}
    for relation in relations:
        # extract persons and happiness units from text
        (start, sign, happiness, end) = re.search(r'^(\w+).*(lose|gain) (\d+).+?(\w+).$', relation).groups()

        if sign == 'lose':
            happiness = int(happiness) * -1

        # make sure the locations exists in the graph
        if not start in graph:
            graph[start] = {}
        if not end in graph:
            graph[end] = {}

        # save the happiness between the locations for both locations
        graph[start][end] = int(happiness) 

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

        permutation.append(permutation[0])

        # add the distance between every person
        for i in range(0, len(permutation) - 1):
            (start, end) = permutation[i:i + 2]

            distance += graph[start][end]
            distance += graph[end][start]

        distances.append(distance)

    return distances

def part1(relations):
    graph = getGraph(relations)

    distances = getGraphDistances(graph)
    distances.sort()

    return distances[-1]

def part2(relations):
    graph = getGraph(relations)

    # save a list of name of every person
    people = list(graph.keys())

    # add me to every persons relations
    for name, relations in graph.items():
        graph[name]['me'] = 0

    # add me to the graph with a relation of 0 with everybody
    graph['me'] = dict(zip(people, [0] * len(people)))

    distances = getGraphDistances(graph)
    distances.sort()

    return distances[-1]

start = time.time()
print("Solution to part 1: %s" % part1(relations))
print("Duration: %s seconds" % str(time.time() - start))

start = time.time()
print("Solution to part 2: %s" % part2(relations))
print("Duration: %s seconds" % str(time.time() - start))