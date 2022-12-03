from string import ascii_lowercase, ascii_uppercase

with open("day03.txt") as f:
    inputs = f.read().splitlines()

values: str = ascii_lowercase + ascii_uppercase


# Part 1 - Identify the priority item in each backpack
def matching(text: str) -> str:
    first_half: str = text[:len(text) // 2]
    second_half: str = text[len(text) // 2:]
    intersect: str = (set(first_half) & set(second_half)).pop()
    return intersect


matches = [matching(text) for text in inputs]
print(sum(values.index(x) + 1 for x in matches))

# Part 2 - Identify the common identity badge in each group of 3 elfs

groups = [inputs[i:i + 3] for i in range(0, len(inputs), 3)]

badges = ""
for each in groups:
    ident = list(set(each[0]) & set(each[1]) & set(each[2]))
    badges += ident[0]

print(sum(values.index(x) + 1 for x in badges))

