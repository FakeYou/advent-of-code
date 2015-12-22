# http://adventofcode.com/day/22

import sys
import time
import itertools
from pprint import pprint

player = { 'hitpoints': 50, 'damage': 0, 'armour': 0, 'mana': 500 }
boss = { 'hitpoints': 55, 'damage': 8, 'armour': 0 }

spellbook = {
    'magic missile': { 'name': 'magic missile', 'cost': 53, 'damage': 4 },
    'drain': { 'name': 'drain', 'cost': 73, 'damage': 2, 'health': 2 },
    'shield': { 'name': 'shield', 'cost': 113, 'effect': { 'name': 'shield', 'armour': 7, 'turns': 6 } },
    'poison': { 'name': 'poison', 'cost': 173, 'effect': { 'name': 'poison', 'damage': 3, 'turns': 6 } },
    'recharge': { 'name': 'recharge', 'cost': 229, 'effect': { 'name': 'recharge', 'mana': 101, 'turns': 5 } }
}

effects = {}

# simulate a fight between the player and an enemy
# returns True when the player wins
def fight(player, spells, enemy):
    totalManaCost = 0

    for turn in range(1000):
        player['armour'] = 0
        # print('-- Turn %d --' % turn)
        # print('- Player has %d hit points, %d armour, %d mana' % (player['hitpoints'], player['armour'], player['mana']))
        # print('- Enemy has %d hit points' % boss['hitpoints'])

        # print('-- Effects --')
        for effect in list(effects.values()):
            if 'armour' in effect:
                player['armour'] = effect['armour']
                # print('%s adds %d armour' % (effect['name'], effect['armour']))

            if 'damage' in effect:
                enemy['hitpoints'] -= max(1, effect['damage'] - enemy['armour'])
                # print('%s deals %d damage' % (effect['name'], max(1, effect['damage'] - enemy['armour'])))

            if 'mana' in effect:
                # print('%s adds %d mana' % (effect['name'], effect['mana']))
                player['mana'] += effect['mana']

            effect['turns'] -= 1
            # print('%s\'s timer is %s' % (effect['name'], effect['turns']))

            if effect['turns'] == 0:
                del effects[effect['name']]

        if enemy['hitpoints'] <= 0:
            # print('player wins')
            return totalManaCost
        if player['hitpoints'] <= 0:
            # print('enemy wins')
            return -1

        if turn % 2 == 0:
            # print('-- Player turn --')
            if len(spells) == 0:
                # print('enemy wins')
                return -1

            spell = spells.pop()

            if player['mana'] < spell['cost'] or ('effect' in spell and spell['effect']['name'] in effects):
                # print('enemy wins')
                return -1

            # print(['spell', spell['name']])
            # print(['effects', effects])

            # print('player casts %s' % spell['name'])

            player['mana'] -= spell['cost']
            totalManaCost += spell['cost']

            if 'damage' in spell:
                enemy['hitpoints'] -= max(1, spell['damage'] - enemy['armour'])
                # print('player deals %d damage' % (max(1, enemy['damage'] - player['armour'])))

            if 'health' in spell:
                player['hitpoints'] += spell['health']
                # print('player heals %d healt' % spell['health'])

            if 'effect' in spell:
                effects[spell['effect']['name']] = spell['effect'].copy()
        else:
            # print('-- Enemy turn --')
            player['hitpoints'] -= max(1, enemy['damage'] - player['armour'])
            # print('enemy deals %d damage' % (max(1, enemy['damage'] - player['armour'])))

        if enemy['hitpoints'] <= 0:
            # print('player wins')
            return totalManaCost
        if player['hitpoints'] <= 0:
            # print('enemy wins')
            return -1

        # print('')

spells = [
    spellbook['magic missile'],
    spellbook['poison'],
    spellbook['drain'],
    spellbook['shield'],
    spellbook['recharge'],
]
# print(fight(player.copy(), spells, boss.copy()))

def part1(player, boss):
    spell_combinations = itertools.product(list(spellbook.values()), repeat=11)
    lowestManaCost = sys.maxsize

    print(len(list(spell_combinations)))

    for spells in spell_combinations:
        cost = fight(player.copy(), list(spells), boss.copy())

        if cost is not -1:
            if cost < lowestManaCost:
                pprint(list(spells))
                print(cost)
                print('---')
            lowestManaCost = min(lowestManaCost, cost)

    print(lowestManaCost)

part1(player, boss)