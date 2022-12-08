"""
Pb: https://adventofcode.com/2022/day/7

Part 1:
------
It's a graph traversal

Part 2:
------

"""

import os

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILE = "data/day7_filesystem.txt"


class Node(object):

    """Docstring for Node."""

    def __init__(self, parent, node_type, name, size=0):
        self.parent = parent
        self.name = name
        self.node_type = node_type
        self.children = []
        self.size = size

    def __str__(self):
        return f"{self.node_type} : {self.name} : {str(self.get_size())}"

    def __repr__(self):
        return f"{self.node_type} : {self.name} : {str(self.get_size())}"

    def get_size(self):
        if self.node_type == "file":
            return self.size
        else:
            return sum(child.get_size() for child in self.children)


def measure(root):
    """
    Measure size of directories of size < 100000
    """
    tot = 0

    def traverse(node):
        nonlocal tot
        if not node:
            return
        if node.node_type == "dir" and node.get_size() < 100000:
            tot += node.get_size()
        for child in node.children:
            traverse(child)

    traverse(root)
    return tot


def find_smallest(root, threshold):
    """
    Find smalles directory  of size > threshold
    """
    min_ = 10000000000000000000

    def traverse(node):
        nonlocal min_
        if not node:
            return
        if node.node_type == "dir" and node.get_size() > threshold:
            min_ = min(min_, node.get_size())
        for child in node.children:
            traverse(child)

    traverse(root)
    return min_


def solution_1(input_file_path: str) -> int:
    rv = 0
    root = Node(None, "dir", "dummy", 0)
    curr = root

    relative_path = input_file_path
    path = os.path.join(SCRIPT_DIR, relative_path)

    with open(path, "r") as input_file:
        for line in input_file:
            line = line.rstrip()
            if "cd" in line and line.split(" ")[1] == "cd":
                if line.split(" ")[-1] == "/":
                    curr = Node(curr, "dir", "/", 0)
                    root.children.append(curr)
                elif line.split(" ")[-1] == "..":
                    curr = curr.parent
                else:
                    dir_name = line.split(" ")[-1]
                    try:
                        curr = next(
                            (node for node in curr.children if node.name == dir_name)
                        )
                    except StopIteration:
                        import ipdb

                        ipdb.set_trace()
                        print("PB")
            elif "dir" in line:
                dir_name = line.split(" ")[-1]
                curr.children.append(Node(curr, "dir", dir_name, 0))
            elif line == "$ ls":
                pass
            else:
                file_name = line.split(" ")[-1]
                size = line.split(" ")[0]
                curr.children.append(Node(curr, "file", file_name, int(size)))

    print(measure(root))
    unused_space = 70000000 - root.get_size()
    required_space = 30000000 - unused_space
    print(find_smallest(root, threshold=required_space))

    return rv


solution_1(INPUT_FILE)
