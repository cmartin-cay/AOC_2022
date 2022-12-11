from collections import deque
from dataclasses import dataclass
from operator import mul
from math import floor, lcm
import re


@dataclass
class Monkey:
    items: deque
    operation: list
    test: int
    throw: list[int]
    inspection_count: int = 0

    def inspect(self):
        while self.items:
            item = self.items.popleft()
            self.inspection_count += 1
            item = self.operate(item)
            item = item % 9699690
            if item % self.test == 0:
                other = monkey_list[self.throw[0]]
                other.items.append(item)
            else:
                other = monkey_list[self.throw[1]]
                other.items.append(item)

    def operate(self, item):
        val = self.operation[1]
        val = val if isinstance(val, int) else item
        if self.operation[0] == "*":
            return item * val
        else:
            return item + val


monkey_list = []

with open("day11.txt") as f:
    for monkey in f.read().strip().split("\n\n"):
        _, inventory, op, *test = monkey.split("\n")
        inventory = re.findall(r"\d+", inventory)
        inventory = [int(x) for x in inventory]
        operation = op.split()[-2:]
        ops = [int(x) if x.isdigit() else x for x in operation]
        test_vals = []
        for t in test:
            vals = re.findall(r"\d+", t)
            test_vals.extend(vals)
        monkey = Monkey(items=deque(inventory),
                        operation=ops,
                        test=int(test_vals[0]),
                        throw=[int(test_vals[1]), int(test_vals[2])])
        monkey_list.append(monkey)


for _ in range(10000):
    for monkey in monkey_list:
        monkey.inspect()

most_inspctions = sorted(monkey.inspection_count for monkey in monkey_list)[-2:]
print(most_inspctions[0]*most_inspctions[1])

# test_vals = [monkey.test for monkey in monkey_list]
# print(test_vals)
# print(lcm(*test_vals))