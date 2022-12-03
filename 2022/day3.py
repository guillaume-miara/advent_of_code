"""
Pb: https://adventofcode.com/2022/day/3

Part 1:
------
Rucksack with 2 compartments.
Should be exactly one type of item per rucksack and it's messed up for every
ruckack for one item

List of all items per rucksack
One line per rucksack: divided in 2 compartments
Count all unique items priority: 

Solution: Brute forcing as usual

Part 2:
------

Elves divided into groups of 3
Every elf has an identifying badge: a unique item type they all carry

Every group is 3 lines

Count priority of badges

"""

import os

SCRIPT_DIR = os.path.dirname(__file__)


def _get_priority(char: str) -> int:
    if char.islower():
        return ord(char) - ord("a") + 1
    return ord(char) - ord("A") + 27


def solution_1(input_file_path: str) -> int:
    rv = 0

    relative_path = input_file_path
    path = os.path.join(SCRIPT_DIR, relative_path)

    with open(path, "r") as input_file:
        for line in input_file:
            rucksack = line.rstrip()
            rlen = len(rucksack) // 2
            r1, r2 = rucksack[:rlen], rucksack[rlen:]
            item = set(r1).intersection(set(r2)).pop()
            print(item, _get_priority(item))
            rv += _get_priority(item)

    print(rv)
    return rv


def solution_2(input_file_path: str) -> int:
    rv = 0
    c = 0
    sets = []

    relative_path = input_file_path
    path = os.path.join(SCRIPT_DIR, relative_path)

    with open(path, "r") as input_file:
        for line in input_file:
            c += 1
            rucksack = line.rstrip()
            sets.append(set(rucksack))
            if c == 3:
                item = set.intersection(*sets).pop()
                rv += _get_priority(item)
                sets = []
                c = 0

    print(rv)
    return rv


solution_1("data/day3_rucksack.txt")
solution_2("data/day3_rucksack.txt")
