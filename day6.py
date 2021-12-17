from aocd.models import Puzzle
from collections import deque

puzzle = Puzzle(year=2021, day=6)
fish_data = puzzle.input_data

days = 256
fish_buckets = deque([0, 0, 0, 0, 0, 0, 0, 0, 0])
fish_buckets[0] = fish_data.count("0")
fish_buckets[1] = fish_data.count("1")
fish_buckets[2] = fish_data.count("2")
fish_buckets[3] = fish_data.count("3")
fish_buckets[4] = fish_data.count("4")
fish_buckets[5] = fish_data.count("5")
fish_buckets[6] = fish_data.count("6")
fish_buckets[7] = fish_data.count("7")
fish_buckets[8] = fish_data.count("8")

for day in range(days):
    fish_buckets.rotate(-1)
    fish_buckets[6] = fish_buckets[6] + fish_buckets[8]


print(sum(fish_buckets))
