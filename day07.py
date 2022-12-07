from collections import deque, defaultdict
from itertools import accumulate

path_history = deque(["/"])
current_directory = ""
dirs = list("/")
dirs_size = defaultdict(int)

with open("day07.txt") as f:
    commands = f.readlines()
    commands = [x.rstrip() for x in commands]

for command in commands:
    instructions = command.split()
    # Deal with the $ commands - changing directory level
    if instructions[0] == "$":
        # Root
        if instructions[1] == "cd" and instructions[2] == "/":
            continue
        # Moving to a new directory
        elif instructions[1] == "cd" and instructions[2].isalpha():
            path_history.append(instructions[2])
            # print(f"{path_history=}")
        # Moving back up to a parent directory
        elif instructions[1] == "cd" and instructions[2] == "..":
            path_history.pop()
            # print(f"{path_history=}")
        else:
            continue
    elif instructions[0] == "dir":
        continue
    elif int(instructions[0]):
        for each in accumulate(path_history):
            dirs_size[each] += int(instructions[0])
    # print(f"{path_history=}")


small = sum(v for k, v in dirs_size.items() if v <= 100000)
print(small)

total_size = 70000000
needed_size = 30000000
unused_space = total_size - dirs_size["/"]
threshold = needed_size - unused_space
print(threshold)

available = sorted((v for k, v in dirs_size.items() if v >= threshold))[0]
print(available)
