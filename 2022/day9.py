"""
Pb: https://adventofcode.com/2022/day/9

Part 1:
------

We can create a big enough matrix as an input, 
start in the middle of it and apply the motions 
to determine how many spots are visited

Part 2:
------

"""

import os

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILE = "data/day9_rope.txt"


def move_tail(tail_row, tail_col, head_row, head_col):
    # Moving horizontally
    if tail_row == head_row:
        if head_col > tail_col + 1:
            return (tail_row, tail_col + 1)
        elif head_col < tail_col - 1:
            return (tail_row, tail_col - 1)
        return (tail_row, tail_col)
    # Moving vertically
    elif tail_col == head_col:
        if head_row > tail_row + 1:
            return (tail_row + 1, tail_col)
        elif head_row < tail_row - 1:
            return (tail_row - 1, tail_col)
        return (tail_row, tail_col)
    # Moving diagonally
    else:
        # Moving towards right
        if head_col > tail_col + 1:
            return (head_row, tail_col + 1)
        # Moving towards left
        elif head_col < tail_col - 1:
            return (head_row, tail_col - 1)
        # Moving towards bottom
        elif head_row > tail_row + 1:
            return (tail_row + 1, head_col)
        # Moving towards up
        elif head_row < tail_row - 1:
            return (tail_row - 1, head_col)
        return (tail_row, tail_col)


def solution(input_file_path: str) -> int:
    rv = 0
    N = 1000
    matrix = [[0] * N] * N
    initial_row = N // 2
    initial_col = N // 2
    head_row, head_col = initial_row, initial_col
    tail_row, tail_col = initial_row, initial_col
    visited = set()
    visited.add((tail_row, tail_col))

    relative_path = input_file_path
    path = os.path.join(SCRIPT_DIR, relative_path)

    with open(path, "r") as input_file:
        for line in input_file:
            direction, steps = line.rstrip().split(" ")
            s = int(steps)
            while s > 0:
                if direction == "U":
                    head_row -= 1
                elif direction == "D":
                    head_row += 1
                elif direction == "R":
                    head_col += 1
                elif direction == "L":
                    head_col -= 1
                tail_row, tail_col = move_tail(tail_row, tail_col, head_row, head_col)
                visited.add((tail_row, tail_col))
                s -= 1
    print(len(visited))
    return rv


solution(INPUT_FILE)
