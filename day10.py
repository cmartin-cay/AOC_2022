from math import floor

cycle = 0
x = 1
w = 40
h = 6
matches = []
c_and_x = [(0, 1)]

grid = [["🎄" for p in range(w)] for y in range(h)]

with open('day10.txt') as f:
    instructions = f.readlines()
    instructions = [x.rstrip().split() for x in instructions]

# Part 1
# def add_cycle(cycle):
#     cycle += 1
#     if cycle in [20, 60, 100, 140, 180, 220]:
#         # print(f"{cycle=}, {x=}, {cycle * x}")
#         matches.append(cycle * x)
#     return cycle

# def add_cycle(cycle):
#     global x
#     y = [x-1, x, x+1]
#     print(cycle)
#     if cycle % 40 in y:
#         col = floor(cycle // 20)
#         grid[col][cycle] = "#"
#         # print(grid)
#     cycle += 1
#     return cycle


for instruct in instructions:
    if instruct[0] == "noop":
        cycle += 1
        c_and_x.append((cycle, x))
    elif instruct[0] == "addx":
        cycle += 1
        c_and_x.append((cycle, x))
        cycle += 1
        x += int(instruct[1])
        c_and_x.append((cycle, x))


for cycle, x in c_and_x:
    y = [x - 1, x, x + 1]
    col = floor(cycle // 40)
    # print(col)
    if cycle % 40 in y:
        pass
        grid[col][cycle % 40] = "🎅"



for row in grid:
    print(row)
    print(row)
