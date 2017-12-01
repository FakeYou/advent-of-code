# http://adventofcode.com/day/20

import sys
import time
import itertools
from pprint import pprint

shop = {
    'weapons': [
        { 'name': 'Dagger'     , 'cost': 8   , 'damage': 4 , 'armour': 0} ,
        { 'name': 'Shortsword' , 'cost': 10  , 'damage': 5 , 'armour': 0} ,
        { 'name': 'Warhammer'  , 'cost': 25  , 'damage': 6 , 'armour': 0} ,
        { 'name': 'Longsword'  , 'cost': 40  , 'damage': 7 , 'armour': 0} ,
        { 'name': 'Greataxe'   , 'cost': 74  , 'damage': 8 , 'armour': 0} ,
    ],
    'armour': [
        { 'name': 'Shirt'      , 'cost': 0   , 'damage': 0 , 'armour': 0} ,
        { 'name': 'Leather'    , 'cost': 13  , 'damage': 0 , 'armour': 1} ,
        { 'name': 'Chainmail'  , 'cost': 31  , 'damage': 0 , 'armour': 2} ,
        { 'name': 'Splintmail' , 'cost': 53  , 'damage': 0 , 'armour': 3} ,
        { 'name': 'Bandedmail' , 'cost': 75  , 'damage': 0 , 'armour': 4} ,
        { 'name': 'Platemail'  , 'cost': 102 , 'damage': 0 , 'armour': 5} ,
    ],
    'rings': [
        { 'name': 'Nothing +1' , 'cost': 0   , 'damage': 0 , 'armour': 0} ,
        { 'name': 'Damage +1'  , 'cost': 25  , 'damage': 1 , 'armour': 0} ,
        { 'name': 'Damage +2'  , 'cost': 50  , 'damage': 2 , 'armour': 0} ,
        { 'name': 'Damage +3'  , 'cost': 100 , 'damage': 3 , 'armour': 0} ,
        { 'name': 'Defense +1' , 'cost': 20  , 'damage': 0 , 'armour': 1} ,
        { 'name': 'Defense +2' , 'cost': 40  , 'damage': 0 , 'armour': 2} ,
        { 'name': 'Defense +3' , 'cost': 80  , 'damage': 0 , 'armour': 3}
    ]
}

player = { 'hitpoints': 100, 'damage': 0, 'armour': 0 }
boss = { 'hitpoints': 103, 'damage': 9, 'armour': 2 }

# simulate a fight between the player and an enemy
# returns True when the player wins
def fight(player, enemy):
    for turn in range(1000):
        if turn % 2 == 0:
            enemy['hitpoints'] -= max(1, player['damage'] - enemy['armour'])
        else:
            player['hitpoints'] -= max(1, enemy['damage'] - player['armour'])

        if enemy['hitpoints'] < 0 or player['hitpoints'] < 0:
            return player['hitpoints'] > 0

def part1(shop, player, boss):
    # create every posisble item combination with two rings
    equipments = list(itertools.product(*
        [shop['weapons'], shop['armour'], shop['rings'], shop['rings']
    ]))

    lowestCost = sys.maxsize

    for equipment in equipments:
        # twice the same ring is not allowed
        if equipment[2] is equipment[3]:
            continue

        cost = 0
        # apply item bonuses to the player
        build = player.copy()
        for item in equipment:
            build['armour'] += item['armour']
            build['damage'] += item['damage']
            cost += item['cost']

        # save the lowest cost when the fight is won
        if fight(build, boss.copy()):
            lowestCost = min(lowestCost, cost)

    return lowestCost

def part2(shop, player, boss):
    # create every posisble item combination with two rings
    equipments = list(itertools.product(*[
        shop['weapons'], shop['armour'], shop['rings'], shop['rings']
    ]))

    highestCost = 0

    for equipment in equipments:
        # twice the same ring is not allowed
        if equipment[2] is equipment[3]:
            continue

        cost = 0
        # apply item bonuses to the player
        build = player.copy()
        for item in equipment:
            build['armour'] += item['armour']
            build['damage'] += item['damage']
            cost += item['cost']

        # save the highest cost when the fight is lost
        if not fight(build, boss.copy()):
            highestCost = max(highestCost, cost)

    return highestCost

start = time.time()
print("Solution to part 1: %s" % part1(shop, player, boss))
print("Duration: %s seconds" % str(time.time() - start))

start = time.time()
print("Solution to part 2: %s" % part2(shop, player, boss))
print("Duration: %s seconds" % str(time.time() - start))
