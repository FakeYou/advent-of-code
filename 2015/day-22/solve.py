# http://adventofcode.com/day/22

import sys
import time
import random
import itertools
from pprint import pprint

PLAYER_HP      = 0
PLAYER_MANA    = 1
BOSS_HP        = 2
BOSS_DAMAGE    = 3
TOTAL_MANA     = 4
SHIELD_TIMER   = 5
POISON_TIMER   = 6
RECHARGE_TIMER = 7
CURSE_DAMAGE   = 8

begin = [
    50,     # player hp
    500,    # player mana
    55,     # boss hp
    8,      # boss damage
    0,      # total mana cost
    0,      # shield timer
    0,      # poison timer
    0,      # recharge timer
    0       # curse damage
]

costs = { 'm': 53, 'd': 73, 's': 113, 'p': 173, 'r': 229 }

global lowest_mana_cost
lowest_mana_cost = sys.maxsize

def effects(status):
    if status[POISON_TIMER] > 0:
        status[BOSS_HP] -= 3

    if status[RECHARGE_TIMER] > 0:
        status[PLAYER_MANA] += 101

    status[SHIELD_TIMER] = max(0, status[SHIELD_TIMER] - 1)
    status[POISON_TIMER] = max(0, status[POISON_TIMER] - 1)
    status[RECHARGE_TIMER] = max(0, status[RECHARGE_TIMER] - 1)

# method to simulate one round of attacks, one turn for the player
# and one turn for the boss
# return a tuple of (Boolean, Array)
#
# the boolean indicates wether the fight was won or lost (True or False)
# when it it is None then the fight didn't finish yet
#
# The array is the status of the fight after this round
def round(spell, status):
    # -- Player turn --

    status[PLAYER_HP] -= status[CURSE_DAMAGE]
    if status[PLAYER_HP] <= 0:
        return (False, status)

    # apply effects before casting a spell
    effects(status)

    if status[BOSS_HP] <= 0:
        return (True, status)

    # make sure that the player has enough mana
    if costs[spell] > status[PLAYER_MANA]:
        return (False, status)

    status[PLAYER_MANA] -= costs[spell]
    status[TOTAL_MANA] += costs[spell]

    # 'Magic missile' instantly does 4 damage
    if spell == 'm':
        status[BOSS_HP] -= 4
    # 'Drain' instantly does 2 damage and heals 4 hp
    if spell == 'd':
        status[BOSS_HP] -= 2
        status[PLAYER_HP] += 2
    # 'Shield' creates a magic shield giving +7 armour for 6 turns 
    if spell == 's':
        status[SHIELD_TIMER] = 6
    # 'Poison' poisons the enemy dealing 3 damage every turn for 6 turns
    if spell == 'p':
        status[POISON_TIMER] = 6
    # 'Recharge' gives 101 mana every turn for 5 turns
    if spell == 'r':
        status[RECHARGE_TIMER] = 5

    if status[BOSS_HP] <= 0:
        return (True, status)

    # -- Boss turn --

    # apply effects before attacking
    effects(status)

    if status[BOSS_HP] <= 0:
        return (True, status)

    # if the 'Shield' effect is active then the player gains 7 armour
    shield = 7 if status[SHIELD_TIMER] > 0 else 0
    status[PLAYER_HP] -= max(1, status[BOSS_DAMAGE] - shield)

    if status[PLAYER_HP] <= 0:
        return (False, status)

    return (None, status)

# recursive function to find the cheapest winning combination of spells
# it will simulate one round of fight with each possible spell and save the 
# status. Then it will call itself with the list of previous spells and the new 
# status. When the fight is won it checks the total mana cost
def fight(spells, status):
    global lowest_mana_cost

    # branch for every spell in the spellbook
    # r: Recharge, p: Poison, s: Shield, m: Magic Missile, d: Drain
    for spell in 'rpsmd':
        _status = status.copy()

        # skip when the spell is too expensive even after a mana boost
        if costs[spell] > _status[PLAYER_MANA] + 110:
            continue
        # skip Shield spell if the shield effect is still active
        if spell == 's' and _status[SHIELD_TIMER] > 1:
            continue
        # skip Poison spell if the poison effect is still active
        if spell == 'p' and _status[POISON_TIMER] > 1:
            continue
        # skip Recharge spell if the recharge effect is still active
        if spell == 'r' and _status[RECHARGE_TIMER] > 1:
            continue

        (finished, new_status) = round(spell, _status)

        # if this branch is already more expensive than the cheapest one then 
        # don't bother simulating any further
        if new_status[TOTAL_MANA] > lowest_mana_cost:
            continue

        # save the lowest mana cost after the fight is won
        if finished is True:
            lowest_mana_cost = min(lowest_mana_cost, new_status[TOTAL_MANA])
        # recurse if the fight isn't decided yet
        if finished is None:
            fight(spells + spell, new_status)

def part1(begin):
    global lowest_mana_cost
    lowest_mana_cost = sys.maxsize

    fight('', begin)

    return lowest_mana_cost

def part2(begin):
    global lowest_mana_cost
    lowest_mana_cost = sys.maxsize

    begin = begin.copy()
    begin[CURSE_DAMAGE] = 1

    fight('', begin)

    return lowest_mana_cost

start = time.time()
print("Solution to part 1: %s" % part1(begin))
print("Duration: %s seconds" % str(time.time() - start))

start = time.time()
print("Solution to part 2: %s" % part2(begin))
print("Duration: %s seconds" % str(time.time() - start))
