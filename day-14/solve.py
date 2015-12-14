# http://adventofcode.com/day/14

import re
import time
from pprint import pprint
from collections import Counter

input = open('input.txt').read()
routes = input.split('\n')

# create an array of reindeers with the values (name, speed, flytime, resttime)
pattern = re.compile(r'^(\w*) can fly (\d*) km/s for (\d*) seconds, but then must rest for (\d*) seconds.$', re.MULTILINE)
reindeers = pattern.findall(input)

# returns the distances of all reindeer at a given moment
def getDistancesAtTime(endtime, reindeers):
    distances = Counter()

    # loop through every reindeer and calculate its distance
    for reindeer in reindeers:
        time = 0
        distance = 0
        (speed, flytime, resttime) = list(map(int, reindeer[1:]))

        # add the speed * flytime to the distance while the time is less then the endtime
        while time < endtime:
            # if the next period of flying exceeds the endtime then we limit the flytime
            # to the time left until the endtime
            if time + flytime > endtime:
                flytime -= time + flytime - endtime

            distance += speed * flytime
            time += flytime
            time += resttime

        # save the distance in the counter per reindeer
        distances[reindeer[0]] = distance

    return distances

def part1(racetime, reindeers):
    # get the distance of each reindeer at the end of the racetime
    distances = list(getDistancesAtTime(racetime, reindeers).values())

    # sort from smallest to largest
    distances.sort()

    # return the largest value
    return distances[-1]

def part2(racetime, reindeers):
    scores = Counter()

    # for every second in the racetime calculate the distance of each reindeer
    # award a point to every reindeer who is in front at every second
    for time in range(1, racetime + 1):
        score = getDistancesAtTime(time, reindeers)

        # get the distance of each reindeer from highest to lowest
        points = score.most_common()
        # filter the points to only include the reindeer in front
        points = dict((key, 1) for key, val in dict(points).items() if val == points[0][1])

        # add 1 point to the total score for every reindeer in front
        scores += Counter(points)

    # return the score of the reindeer in front
    return scores.most_common(1)[0][1]

start = time.time()
print("Solution to part 1: %s" % part1(2503, reindeers))
print("Duration: %s seconds" % str(time.time() - start))

start = time.time()
print("Solution to part 2: %s" % part2(2503, reindeers))
print("Duration: %s seconds" % str(time.time() - start))