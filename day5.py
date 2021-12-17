import re
import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=5)
data = puzzle.input_data.splitlines()
split_data = [re.split(",|\s->\s", segment) for segment in data]
line_segments = np.zeros((1000, 1000))
solution = 0


class LineSegmentCoord:
    duplicate_x = False
    duplicate_y = False
    diagonal = False

    def __init__(self, points: list[str]) -> None:
        self.points = points
        self.int_points = [int(point) for point in self.points]
        pass

    def check_duplicate_x_coord(self) -> bool:
        return self.points[0] == self.points[2]

    def check_duplicate_y_coord(self) -> bool:
        return self.points[1] == self.points[3]

    def check_diagonal_coord(self) -> bool:
        return abs(self.int_points[0] - self.int_points[2]) == abs(
            self.int_points[1] - self.int_points[3]
        )

    def check_duplicate_coord(self) -> bool:
        self.duplicate_x = self.check_duplicate_x_coord()
        self.duplicate_y = self.check_duplicate_y_coord()
        self.diagonal = self.check_diagonal_coord()

    def line_segment_coord(self) -> list[int]:
        draw_line = []
        x_coords = []
        y_coords = []
        if self.duplicate_x:
            y_coords = sorted([self.int_points[1], self.int_points[3]])
            for i in range(y_coords[0], y_coords[1] + 1):
                draw_line.append([self.int_points[0], i])

        if self.duplicate_y:
            x_coords = sorted([self.int_points[0], self.int_points[2]])
            for i in range(x_coords[0], x_coords[1] + 1):
                draw_line.append([i, self.int_points[1]])

        if self.diagonal:
            if self.int_points[1] < self.int_points[3]:
                if self.int_points[0] < self.int_points[2]:
                    for i in range((self.int_points[2] - self.int_points[0]) + 1):
                        draw_line.append(
                            [(i + self.int_points[0]), (i + self.int_points[1])]
                        )
                else:
                    for i in range((self.int_points[0] - self.int_points[2]) + 1):
                        draw_line.append(
                            [(i + self.int_points[2]), (self.int_points[3] - i)]
                        )
            if self.int_points[3] < self.int_points[1]:
                if self.int_points[0] < self.int_points[2]:
                    for i in range((self.int_points[2] - self.int_points[0]) + 1):
                        draw_line.append(
                            [(i + self.int_points[0]), (self.int_points[1] - i)]
                        )
                else:
                    for i in range((self.int_points[0] - self.int_points[2]) + 1):
                        draw_line.append(
                            [(i + self.int_points[2]), (i + self.int_points[3])]
                        )
        return draw_line


# test_data = [
#     ["0", "9", "5", "9"],
#     ["8", "0", "0", "8"],
#     ["9", "4", "3", "4"],
#     ["2", "2", "2", "1"],
#     ["7", "0", "7", "4"],
#     ["6", "4", "2", "0"],
#     ["0", "9", "2", "9"],
#     ["3", "4", "1", "4"],
#     ["0", "0", "8", "8"],
#     ["5", "5", "8", "2"],
#     ["1", "1", "3", "3"],
#     ["9", "7", "7", "9"],
# ]

for points in split_data:
    draw_coord = []
    draw_segment = LineSegmentCoord(points)
    draw_segment.check_duplicate_coord()
    if draw_segment.line_segment_coord():
        draw_coord = draw_segment.line_segment_coord()
        # print(draw_coord)
    for point in draw_coord:
        line_segments[point[0]][point[1]] += 1
# print(line_segments)

for x in range(1000):
    for y in range(1000):
        if line_segments[x][y] > 1:
            solution += 1

print(solution)
