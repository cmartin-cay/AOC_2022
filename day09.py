from dataclasses import dataclass, field
from math import dist, floor

with open("day09.txt") as f:
    instructions = f.readlines()
    instructions = [x.strip().split() for x in instructions]


@dataclass
class Knot:
    x_pos: int = 0
    y_pos: int = 0
    visited: set[tuple[int, int]] = field(default_factory=set)

    def move(self, direction):
        direction_dict = {"U": (self.x_pos, self.y_pos - 1),
                          "D": (self.x_pos, self.y_pos + 1),
                          "L": (self.x_pos - 1, self.y_pos),
                          "R": (self.x_pos + 1, self.y_pos)
                          }
        self.x_pos, self.y_pos = direction_dict[direction]

    def distance(self, other: "Knot"):
        return (self.x_pos - other.x_pos, self.y_pos - other.y_pos)


@dataclass
class Tail(Knot):
    def is_touching(self, other):
        # The Chebyshev distance (kings move distance) should work here
        distance = max(abs(self.x_pos - other.x_pos), abs(self.y_pos - other.y_pos))
        if distance > 1:
            return False
        else:
            return True

    def chase(self, other):
        separation = self.distance(other)
        x_distance, y_distance = separation
        if not self.is_touching(other):
            if abs(x_distance) >= 1 and abs(y_distance) >= 1:
                self.x_pos -= x_distance if x_distance == 1 else x_distance // 2
                self.y_pos -= y_distance if y_distance == 1 else y_distance // 2
            elif abs(x_distance) > 1:
                self.x_pos -= x_distance // 2
            elif abs(y_distance) > 1:
                self.y_pos -= y_distance // 2
            self.visited.add((self.x_pos, self.y_pos))


# Part 1 - A rope with a head knot and tail knot
head = Knot()
tail = Tail()
tail.visited.add((0, 0))
for elem in instructions:
    for _ in range(int(elem[1])):
        head.move(elem[0])
        tail.chase(head)
print(len(tail.visited))

# Part 2 - We now have a rope with a head knot and 9 tail knots
knots = []
head = Knot()
knots.append(head)
for _ in range(9):
    tail = Tail()
    tail.visited.add((0, 0))
    knots.append(tail)

for elem in instructions:
    for _ in range(int(elem[1])):
        head.move(elem[0])
        for i in range(1, len(knots)):
            knots[i].chase(knots[i - 1])

print(len(knots[-1].visited))
