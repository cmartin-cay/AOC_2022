from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int


with open("day14.txt") as infile:
    f = infile.readlines()
    f = [f.strip().split(" -> ") for f in f]
    f = [[x.split(",") for x in y] for y in f]
    f = [[x for x in y] for y in f]
    f = [[Point(int(x[0]), int(x[1])) for x in y] for y in f]
    print(f)

cave = set()


def straight_line(start: Point, end: Point):
    if start.x == end.x:
        x_dir = 0
    else:
        x_dir = 1 if end.x > start.x else -1
    if start.y == end.y:
        y_dir = 0
    else:
        y_dir = 1 if end.y > start.y else -1
    if x_dir:
        for x in range(start.x, end.x, x_dir):
            yield Point(x, start.y)
    if y_dir:
        for y in range(start.y, end.y, y_dir):
            yield Point(start.x, y)


a = Point(0, 0)
b = Point(0, 5)

cave.add(a)
cave.add(b)

res = straight_line(a, b)
print(res)
for elem in res:
    cave.add(elem)

print(cave)
