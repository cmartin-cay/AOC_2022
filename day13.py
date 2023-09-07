import ast

with open("day05.txt") as f:
    pairs = f.read().split("\n\n")
    pairs = [pair.split("\n") for pair in pairs]
    left_vals = []
    right_vals = []
    for pair in pairs:
        left_vals.append(ast.literal_eval(pair[0]))
        right_vals.append(ast.literal_eval(pair[1]))

print(left_vals[4])
print(right_vals[4])


def in_order(l1, l2):
    if isinstance(l1, int) and isinstance(l2, int):
        if l1 == l2:
            return None
        return l1 < l2

    if isinstance(l1, list) and isinstance(l2, list):
        for e1, e2 in zip(l1, l2):
            if (comparison := in_order(e1, e2)) is not None:
                return comparison
        return in_order(len(l1), len(l2))

    if isinstance(l1, int):
        return in_order([l1], l2)
    return in_order(l1, [l2])


print(in_order(left_vals[4], right_vals[4]))
