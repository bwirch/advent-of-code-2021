from posixpath import split
from aocd.models import Puzzle
from collections import Counter

puzzle = Puzzle(year=2021, day=7)
data = puzzle.input_data.splitlines()
split_data = data[0].split(",")
crab_data = [int(pos) for pos in split_data]
# crab_data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
crab_data.sort()
max_range = crab_data[len(crab_data) - 1]
min_movement = 9999999999999999

crab_count = Counter()
for crab_pos in crab_data:
    crab_count[crab_pos] += 1

for i in range(max_range):
    total_movement = 0
    for crab_pos in crab_count:
        step = abs(crab_pos - i)
        # movement = step * crab_count[crab_pos]
        movement = ((step ** 2 + step) / 2) * crab_count[crab_pos]
        total_movement = total_movement + movement

    if total_movement < min_movement:
        min_movement = total_movement


print(min_movement)
