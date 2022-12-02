scores = {"X": 1, "Y": 2, "Z": 3}
convert = {"A": "X", "B": "Y", "C": "Z"}
draw = 3
win = 6
lose = 0
total = 0

"""
X = ROCK
Y = PAPER
Z = SCISSORS
"""
result_table = {
    ("X", "Y"): win,
    ("Y", "X"): lose,
    ("Y", "Z"): win,
    ("Z", "Y"): lose,
    ("Z", "A"): lose,
    ("A", "Z"): win,
    ("X", "Z"): lose,
    ("Z", "X"): win
}

win_table = {"X": "Z",
             "Y": "X",
             "Z": "Y"
             }
lose_table = {v: k for k, v in win_table.items()}

with open("day02.txt") as f:
    rounds = f.read().splitlines()


# Part 1 - Play To Win
def play_game(opponent: str, hero: str) -> int:
    opponent = convert[opponent]
    if opponent == hero:
        return draw + scores[hero]
    else:
        return result_table[(opponent, hero)] + scores[hero]


for each in rounds:
    total += play_game(opponent=each[0], hero=each[2])

print(total)

# Part 2 - Play Optimal Strategy
"""
X - LOSE
Y - DRAW
Z - WIN
"""
optimal_total = 0


def play_optimal_game(opponent: str, result: str) -> int:
    opponent = convert[opponent]
    hand_score: int = scores[opponent]
    if result == "Y":
        return hand_score + draw
    if result == "X":
        losing_shape = win_table[opponent]
        return scores[losing_shape]
    if result == "Z":
        winning_shape = lose_table[opponent]
        return scores[winning_shape] + win

for each in rounds:
    optimal_total += play_optimal_game(opponent=each[0], result=each[2])

print(optimal_total)
