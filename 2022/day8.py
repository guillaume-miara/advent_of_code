"""
Pb: https://adventofcode.com/2022/day/8

Part 1:
------
We have a matrix of trees. 
For every tree inside, we'll run a `is_visible` check and inc our counter when
it is

"""

import os

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILE = "data/day8_treehouse.txt"


def count_visible_points(matrix) -> int:
    hs = 0
    pos = None
    ROW = len(matrix)
    COL = len(matrix[0])

    for row in range(0, ROW):
        for col in range(0, COL):
            # Outside trees not worth considering because at least one Zero
            if row != 0 and row != ROW - 1 and col != 0 and col != COL - 1:
                tree_height = matrix[row][col]
                l = col - 1
                left_c = 0
                while l >= 0:
                    if matrix[row][l] < tree_height:
                        left_c += 1
                        l -= 1
                    else:
                        left_c += 1
                        break

                r = col + 1
                right_c = 0
                while r < COL:
                    if matrix[row][r] < tree_height:
                        right_c += 1
                        r += 1
                    else:
                        right_c += 1
                        break

                t = row - 1
                top_c = 0
                while t >= 0:
                    if matrix[t][col] < tree_height:
                        top_c += 1
                        t -= 1
                    else:
                        top_c += 1
                        break

                b = row + 1
                bottom_c = 0
                while b < ROW:
                    if matrix[b][col] < tree_height:
                        bottom_c += 1
                        b += 1
                    else:
                        bottom_c += 1
                        break

                scenic_score = left_c * right_c * top_c * bottom_c

                hs = max(scenic_score, hs)
                if hs == scenic_score:
                    pos = (row, col)
                    res = (left_c, right_c, top_c, bottom_c)

    left_c, right_c, top_c, bottom_c = res
    row, col = pos
    print(matrix[row][col])
    print(matrix[row][col - left_c : col])
    print(matrix[row][col + 1 : col + right_c + 2])
    print([matrix[i][col] for i in range(row - top_c, row)])
    print([matrix[i][col] for i in range(row, row + bottom_c + 1)])
    return hs, pos


def highest_scenic_score(matrix) -> int:
    tot = 0
    ROW = len(matrix)
    COL = len(matrix[0])

    for row in range(0, ROW):
        for col in range(0, COL):
            # Only considering inside trees
            if row != 0 and row != ROW - 1 and col != 0 and col != COL - 1:
                tree_height = matrix[row][col]
                vis_left = all(t < tree_height for t in matrix[row][0:col])
                vis_right = all(t < tree_height for t in matrix[row][col + 1 :])
                vis_top = all(
                    t < tree_height for t in [matrix[i][col] for i in range(0, row)]
                )
                vis_bottom = all(
                    t < tree_height
                    for t in [matrix[i][col] for i in range(row + 1, ROW)]
                )
                if any(
                    [
                        vis_left,
                        vis_top,
                        vis_bottom,
                        vis_right,
                    ]
                ):
                    tot += 1

    # Adding edge trees
    tot += 2 * ROW + 2 * (COL - 2)

    return tot


def solution_1(input_file_path: str) -> int:
    rv = 0
    matrix = []

    relative_path = input_file_path
    path = os.path.join(SCRIPT_DIR, relative_path)

    with open(path, "r") as input_file:
        for line in input_file:
            row = line.rstrip()
            matrix.append([int(c) for c in row])

    rv = count_visible_points(matrix)

    print(rv)
    return rv


def solution_2(input_file_path: str) -> int:
    rv = 0
    c = 0
    return rv


solution_1(INPUT_FILE)
solution_2(INPUT_FILE)
