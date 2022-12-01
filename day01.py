with open("day01.txt") as infile:
    calories = infile.read().split("\n\n")
    # calories = [cal.strip("\n") for cal in calories]


elf_list = [[int(meal) for meal in elf.split("\n")] for elf in calories]

# Part 1 - Find the elf with the most calories
biggest_elf = max(sum(elf) for elf in elf_list)
print(biggest_elf)

# Part 2 - Sum the top 3 calorie carrying elfs
biggest_three_elfs = sorted((sum(elf) for elf in elf_list), reverse=True)[:3]
print(sum(biggest_three_elfs))

with open("day01.txt") as f:
    data = [elf.splitlines() for elf in f.read().split("\n\n")]
