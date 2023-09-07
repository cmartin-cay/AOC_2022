from itertools import zip_longest

vals = [
    "1=-0-2",
    "12111",
    "2=0=",
    "21",
    "2=01",
    "111",
    "20012",
    "112",
    "1=-1=",
    "1-12",
    "12",
    "1=",
    "122",
]

simple_vals = ["122", "1="]


def elf_add(nums: list[str]) -> str:
    convert = {"0": 0, "1": 1, "2": 2, "-": -1, "=": -2, None: 0}
    nums = [reversed(num) for num in nums]
    nums = list(zip_longest(*nums))
    print(nums)
    something = [[(convert[val]) for val in x] for x in nums]
    for elem in something:
        print(sum(elem))

elf_add(vals)

# convert = {"0": 0, "1": 1, "2": 2, "-": -1, "=": -2, None: 0}
# inp = "1="
# print(sum([convert[each] for each in inp]))
