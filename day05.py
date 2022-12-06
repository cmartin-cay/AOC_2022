
from collections import deque

stacks = [deque("PLMNWVBH"),
          deque("HQM"),
          deque("LMQFGBDN"),
          deque("GWMQFTZ"),
          deque("PHTM"),
          deque("TGHDJMBC"),
          deque("RVFBNM"),
          deque("SGRMHLP"),
          deque("NCBDP")]

# stacks = [deque("NZ"), deque("DCM"), deque("P")]

with open("day05.txt") as f:
    data = f.read().splitlines()
    moves = data[10:]
    moves = [move.split() for move in moves]
    print(moves[0:4])

# Part 1: Can only move one crate at a time
def move_crates(crates: int, start_stack, end_stack):
    while crates:
        crate = stacks[start_stack - 1].popleft()
        stacks[end_stack - 1].appendleft(crate)
        crates -= 1


# for each in moves:
#     crates = int(each[1])
#     start_stack = int(each[3])
#     end_stack = int(each[5])
#     move_crates(crates=crates, start_stack=start_stack, end_stack=end_stack)

# print("".join(stack[0] for stack in stacks))

# Part 2: A fancier machine can move lots of crates at once
def move_many_crates(crates, start_stack, end_stack):
    stack = deque()
    while crates:
        stack.extendleft(stacks[start_stack-1].popleft())
        crates -= 1
    stacks[end_stack-1].extendleft(stack)

for each in moves:
    crates = int(each[1])
    start_stack = int(each[3])
    end_stack = int(each[5])
    move_many_crates(crates=crates, start_stack=start_stack, end_stack=end_stack)

print("".join(stack[0] for stack in stacks))