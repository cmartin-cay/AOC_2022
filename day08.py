from itertools import accumulate

with open("day08.txt") as f:
    trees = f.readlines()
    trees = [x.rstrip() for x in trees]

horizontal = trees
vertical = ["".join(elem) for elem in list(zip(*trees))]
width = len(trees[0])
height = len(trees)


seen_trees = set()
new_trees = set()

outside_trees = (len(trees[0]) * 2 + len(trees) * 2) - 4

# Step 1 - Add the outside trees to the seen trees set
for x in range(0, width):
    # print(x,0)
    seen_trees.add((0, x))
    seen_trees.add((width - 1, x))
for y in range(0, height):
    seen_trees.add((y, 0))
    seen_trees.add((y, height - 1))

# Step 2 - Traverse each horizontal left and right

for x_pos, each in enumerate(horizontal):
    max_lft = int(each[0])
    max_rt = int(each[-1])
    for y_pos, ht in enumerate(accumulate(each, max)):
        ht = int(ht)
        if ht > max_lft:
            seen_trees.add((x_pos, y_pos))
            max_lft = ht
    for y_pos, ht in enumerate(accumulate(each[::-1], max)):
        ht = int(ht)
        if ht > max_rt:
            seen_trees.add((x_pos, width-y_pos-1))
            max_rt = ht

for y_pos, each in enumerate(vertical):
    max_lft = int(each[0])
    max_rt = int(each[-1])
    for x_pos, ht in enumerate(accumulate(each, max)):
        ht = int(ht)
        if ht > max_lft:
            seen_trees.add((x_pos, y_pos))
            max_lft = ht
    for x_pos, ht in enumerate(accumulate(each[::-1], max)):
        ht = int(ht)
        if ht > max_rt:
            seen_trees.add((height-x_pos-1, y_pos))
            max_rt = ht
print(len(seen_trees))
print(width, height)