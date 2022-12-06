"""
Pb: https://adventofcode.com/2022/day/5

Part 1:
------

Supplies need to be unloaded
They are stored in stacks of marked crates

The crane can move crat between stacks.

Drawing of the stacks and rearrangement procedure

Part 2:
------

"""

import re
import os

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_CRATE_FILE = "data/day5_crates.txt"
INPUT_MOVE_FILE = "data/day5_moves.txt"


def solution_1(input_crates_file_path: str, input_moves_file_path: str) -> int:
    rv = 0

    relative_crate_path = input_crates_file_path
    path = os.path.join(SCRIPT_DIR, relative_crate_path)
    stacks = []

    for line in reversed(list(open(path, "r"))):
        if not stacks:
            stacks = line.rstrip().split(" ")
            stacks = [[] for x in stacks if x]
        else:
            line = line.rstrip()
            ll = len(line)
            i = 1
            s = 0
            while i < ll:
                if line[i] and line[i] != " ":
                    stacks[s].append(line[i])
                i += 4
                s += 1

    relative_move_path = input_moves_file_path
    path = os.path.join(SCRIPT_DIR, relative_move_path)
    for line in list(open(path, "r")):
        line = line.rstrip()
        numbers = re.findall(r"[0-9]+", line)
        moves = int(numbers[0])
        from_ = int(numbers[1])
        to_ = int(numbers[2])
        i = moves
        while i > 0:
            crate = stacks[from_ - 1].pop()
            stacks[to_ - 1].append(crate)
            i -= 1

    rv = "".join([s[-1] for s in stacks])
    print(rv)
    return rv


def solution_2(input_crates_file_path: str, input_moves_file_path: str) -> int:
    rv = 0

    relative_crate_path = input_crates_file_path
    path = os.path.join(SCRIPT_DIR, relative_crate_path)
    stacks = []

    for line in reversed(list(open(path, "r"))):
        if not stacks:
            stacks = line.rstrip().split(" ")
            stacks = [[] for x in stacks if x]
        else:
            line = line.rstrip()
            ll = len(line)
            i = 1
            s = 0
            while i < ll:
                if line[i] and line[i] != " ":
                    stacks[s].append(line[i])
                i += 4
                s += 1

    relative_move_path = input_moves_file_path
    path = os.path.join(SCRIPT_DIR, relative_move_path)
    for line in list(open(path, "r")):
        line = line.rstrip()
        numbers = re.findall(r"[0-9]+", line)
        moves = int(numbers[0])
        from_ = int(numbers[1])
        to_ = int(numbers[2])

        crates = stacks[from_ - 1][-moves:]
        stacks[from_ - 1] = stacks[from_ - 1][:-moves]
        stacks[to_ - 1].extend(crates)

    rv = "".join([s[-1] for s in stacks])
    print(rv)
    return rv


solution_1(INPUT_CRATE_FILE, INPUT_MOVE_FILE)
solution_2(INPUT_CRATE_FILE, INPUT_MOVE_FILE)
