"""
Pb: https://adventofcode.com/2022/day/2

Part1:
------
Rock paper scissors tournament

Rock> Scissors
Scissors > Paper
Paper > Rock
Equals => Draw

A: Rock
B: Paper
C: Scissors

Response:
X: Rock
Y: Paper
Z: Scissors

Scoring for a round: 
shape: 
    - rock: 1
    - Paper: 2
    - Scissors: 3
outcome:
    - lost: 0
    - draw: 3
    - win: 6

Strategy Guide:
    A Y
    B X
    C Z

Objective: Calculate score if choosing strategy guide

Solution:
Brute force calculation of the score line by line
"""

import os

SCRIPT_DIR = os.path.dirname(__file__)

_SHAPE_SCORE = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

_OUTCOME_SCORE = {
    "win": 6,
    "draw": 3,
    "lost": 0,
}

_EVALUATION_GRID = {
    ("A", "X"): "draw",
    ("A", "Y"): "win",
    ("A", "Z"): "lost",
    ("B", "X"): "lost",
    ("B", "Y"): "draw",
    ("B", "Z"): "win",
    ("C", "X"): "win",
    ("C", "Y"): "lost",
    ("C", "Z"): "draw",
}


def _compute_game_score(opp_shape: str, our_shape: str) -> int:
    """
    Compute score without a conversion table: shape1 encrypted as A, B, C
    and shape 2 encrypted as X,Y,Z
    """
    shape_score = _SHAPE_SCORE.get(our_shape)
    outcome = _EVALUATION_GRID.get((opp_shape, our_shape))
    outcome_score = _OUTCOME_SCORE.get(outcome)
    return shape_score + outcome_score


def calculate_total_score(input_file_path: str) -> int:

    rv = 0

    relative_path = input_file_path
    path = os.path.join(SCRIPT_DIR, relative_path)

    with open(path, "r") as input_file:
        for line in input_file:
            game = line.rstrip()
            opp_shape, our_shape = game.split(" ")
            score = _compute_game_score(opp_shape, our_shape)
            rv += score

    print(rv)
    return rv


_REVERSE_EVALUATION_GRID = {
    ("A", "X"): "Z",
    ("A", "Y"): "X",
    ("A", "Z"): "Y",
    ("B", "X"): "X",
    ("B", "Y"): "Y",
    ("B", "Z"): "Z",
    ("C", "X"): "Y",
    ("C", "Y"): "Z",
    ("C", "Z"): "X",
}


def calculate_total_score_part2(input_file_path: str) -> int:

    rv = 0

    relative_path = input_file_path
    path = os.path.join(SCRIPT_DIR, relative_path)

    with open(path, "r") as input_file:
        for line in input_file:
            game = line.rstrip()
            opp_shape, expected_outcome = game.split(" ")
            played_shape = _REVERSE_EVALUATION_GRID.get((opp_shape, expected_outcome))
            score = _compute_game_score(opp_shape, played_shape)
            rv += score

    print(rv)
    return rv


calculate_total_score("data/day2_rock_paper_scissors.txt")
calculate_total_score_part2("data/day2_rock_paper_scissors.txt")
