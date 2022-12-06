from collections import deque

compare = deque(maxlen=4)

# sample = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"

with open("day06.txt") as f:
    sample = f.read()

# Part 1: Listen for a start of message with len 4
for idx, elem in enumerate(sample, start=1):
    compare.extend(elem)
    if len(set(compare)) == 4:
        print(idx)
        break

# Part 2: Listen for a start of message with len 14
compare = deque(maxlen=14)
for idx, elem in enumerate(sample, start=1):
    compare.extend(elem)
    if len(set(compare)) == 14:
        print(idx)
        break