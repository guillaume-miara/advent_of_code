"""
Pb: https://adventofcode.com/2022/day/1

Reindeer eat star fruits
Elves need to get at least 50 star fruits
Fruits are collected solving puzzles. Two per day. Each yield 1 star
=> Need to solve all puzzles

Each elf is carrying calories - represented by a file (stored in /data)

Part 1:
------
Objective: Find the most calories carried by a single elf

My solution:
- we only care about the max
- we need to check the calories for each elve

=> Greedy approach
For every elves:
    - check total calories they have
    - compare to max calories seen so far
    - maybe update max calories
return max calories

Part 2:
------

Now we want to find the total calories carried by the top 3 elves carrying the
most calories

Several options here:
1. Brute force
calc calories for each elves - store the data
Then sort and get top 3
Using a heap or sorting an array is the same thing here - that ends up being an
O(nlogn) operation
2. A bit better is to always keep track of the top3 values and compare curr
   against each of them and reshuffle 
"""

import os

SCRIPT_DIR = os.path.dirname(__file__)


def find_max_calories(calories_file_path: str) -> int:

    rv = 0
    curr = 0

    relative_path = calories_file_path
    path = os.path.join(SCRIPT_DIR, relative_path)

    with open(path, "r") as calories_file:
        for line in calories_file:
            cal = int(line.rstrip() or 0)
            curr += cal
            if not cal:
                rv = max(rv, curr)
                curr = 0

        # Last elf edge case
        rv = max(rv, curr)

    print(rv)
    return rv


def find_top3_calories(calories_file_path: str) -> int:

    rv = 0
    curr = 0

    relative_path = calories_file_path
    path = os.path.join(SCRIPT_DIR, relative_path)

    cals = []

    with open(path, "r") as calories_file:
        for line in calories_file:
            cal = int(line.rstrip() or 0)
            curr += cal
            if not cal:
                cals.append(curr)
                curr = 0
        # Last elf edge case
        cals.append(curr)

    cals.sort()
    top3_sum = sum(cals[-3:])
    print(top3_sum)
    return top3_sum


find_max_calories("data/day1_calories.txt")
find_top3_calories("data/day1_calories.txt")
