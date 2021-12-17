from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=8)
data = puzzle.input_data.splitlines()
codes = []
lengths = []
count = 0

for code in data:

    codes.append(code.split(" | ")[1])

for signal in codes:
    lengths.extend([len(x) for x in signal.split()])

for number in lengths:
    if number <= 4 or number == 7:
        count += 1

print(count)
