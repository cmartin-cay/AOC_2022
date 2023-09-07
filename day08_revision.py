# If we hit a 9 in any direction
# the rest of those trees must be hidden in that direction
from dataclasses import dataclass, field


@dataclass
class Tree:
    x_pos: int
    y_pos: int
    height: int
    visible: bool = False
    vis_score: list[int] = field(default_factory=list)


with open("day08.txt") as f:
    f = f.readlines()
    f = [x.rstrip() for x in f]
    tree_list: list[list[Tree]] = [
        [Tree(x_pos=x_idx, y_pos=y_idx, height=int(j)) for y_idx, j in enumerate(i)]
        for x_idx, i in enumerate(f)
    ]
horizontal = tree_list
vertical = [elem for elem in list(zip(*tree_list))]

first = horizontal[0]
rev_first = first[::-1]


def scan_row(trees):
    rev_trees = trees[::-1]
    check_trees(trees)
    check_trees(rev_trees)


def check_trees(trees):
    prev = None
    for tree in trees:
        if not prev:
            tree.visible = True
            prev = tree
        if tree.height > prev.height:
            tree.visible = True
            prev = tree


for row in horizontal:
    scan_row(row)

for row in vertical:
    scan_row(row)

vis = [sum(1 for j in i if j.visible) for i in tree_list]
print(f"Part 1 {sum(vis)}")

width = len(horizontal[0])
print(f"{width=}")

for row in horizontal:
    for idx, elem in enumerate(row):
        # print(row[:idx])
        print(row[idx:])
        break
