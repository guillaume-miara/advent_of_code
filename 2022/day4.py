"""
Pb: https://adventofcode.com/2022/day/4

Part 1:
------
Cleaning
- each elf has a unique ID #
- Elves are assigned range of section IDs to clean
Assignments overlap

Some assignment fully contains the other one

Part 2:
------

"""

import os

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILE = "data/day4_cleaning.txt"


def contains(s1: str, s2: str) -> bool:
    """Determines if section 1 contains section 2"""
    s1_start, s1_end = [int(n) for n in s1.split("-")]
    s2_start, s2_end = [int(n) for n in s2.split("-")]

    return s1_start <= s2_start and s1_end >= s2_end


def overlap(s1: str, s2: str) -> bool:
    """Determines if section 1 and section 2 overlap"""
    s1_start, s1_end = [int(n) for n in s1.split("-")]
    s2_start, s2_end = [int(n) for n in s2.split("-")]
    if s1_start <= s2_start:
        left = (s1_start, s1_end)
        right = (s2_start, s2_end)
    else:
        right = (s1_start, s1_end)
        left = (s2_start, s2_end)

    if left[1] >= right[0]:
        return True

    return False


def solution_1(input_file_path: str) -> int:
    rv = 0

    relative_path = input_file_path
    path = os.path.join(SCRIPT_DIR, relative_path)

    with open(path, "r") as input_file:
        for line in input_file:
            s1, s2 = line.rstrip().split(",")
            if contains(s1, s2) or contains(s2, s1):
                rv += 1

    print(rv)
    return rv


def solution_2(input_file_path: str) -> int:
    rv = 0

    relative_path = input_file_path
    path = os.path.join(SCRIPT_DIR, relative_path)

    with open(path, "r") as input_file:
        for line in input_file:
            s1, s2 = line.rstrip().split(",")
            if overlap(s1, s2):
                rv += 1

    print(rv)
    return rv


solution_1(INPUT_FILE)
solution_2(INPUT_FILE)
