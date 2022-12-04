# short = list(range(6, 6 + 1))
# long = list(range(4, 6 + 1))

result = 0

with open("day04.txt") as f:
    sectors = f.read().splitlines()
    sectors = [sector.replace("-", ",").split(",") for sector in sectors]
    sectors = [(int(x[0]), int(x[1]), int(x[2]), int(x[3])) for x in sectors]
    # print(sectors)

# Part 1 - How many sectors are entirely covered by another elf
def engulf(sections):
    a = list(range(sections[0], sections[1] + 1))
    b = list(range(sections[2], sections[3] + 1))
    if len(a) > len(b):
        long, short = a, b
    else:
        long, short = b, a
    return 1 if all([elem in long for elem in short]) else 0


for each in sectors:
    result += engulf(each)

print(result)

# Part 2 - Any overlap at all
result = 0
def any_overlap(sections):
    a = set(range(sections[0], sections[1] + 1))
    b = set(range(sections[2], sections[3] + 1))
    return 1 if a & b else 0

for each in sectors:
    result += any_overlap(each)

print(result)