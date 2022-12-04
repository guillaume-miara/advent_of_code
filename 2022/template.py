"""
Pb: https://adventofcode.com/2022/day/4

Part 1:
------

Part 2:
------

"""

import os

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILE = "data/day3_rucksack.txt"


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


solution_1(INPUT_FILE)
solution_2(INPUT_FILE)
