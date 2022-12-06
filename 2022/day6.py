"""
Pb: https://adventofcode.com/2022/day/6

Part 1:
------

Objective: Determine the start of a packet marker in a datastream
4 characters disctinct

It's a sliding window problem

Part 2:
------

"""

import os

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILE = "data/day6_marker.txt"


def _find_marker(string: str, threshold) -> int:
    """
    Returns the first marker position in a string
    """
    chars = {}
    i = 0
    start = 0
    for i, char in enumerate(string):
        # print(i, start, len(chars), chars)
        if char not in chars:
            chars[char] = 1
            # Found the marker
            if len(chars) == threshold:
                return i + 1
        # if char has already been seen, increase start till after chat
        else:
            while start < i:
                v = string[start]
                chars.pop(v)
                start += 1
                if v == char:
                    chars[char] = 1
                    break


def solution_1(input_file_path: str) -> int:
    rv = 0

    relative_path = input_file_path
    path = os.path.join(SCRIPT_DIR, relative_path)

    string_file = open(path, "r")
    string = string_file.read()
    marker = _find_marker(string, 4)
    string_file.close()

    print(marker)
    return rv


def solution_2(input_file_path: str) -> int:
    rv = 0

    relative_path = input_file_path
    path = os.path.join(SCRIPT_DIR, relative_path)

    string_file = open(path, "r")
    string = string_file.read()
    marker = _find_marker(string, 14)
    string_file.close()

    print(marker)
    return rv


solution_1(INPUT_FILE)
solution_2(INPUT_FILE)
