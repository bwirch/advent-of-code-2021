from aocd.models import Puzzle
from dataclasses import dataclass

puzzle = Puzzle(year=2021, day=4)
data = puzzle.input_data.splitlines()
draw_numbers = data[0].split(",")
number_of_boards = int(len(data) / 6)
board_list = []
solution = False


@dataclass
class Cell:
    number: str
    is_dabbed: bool = False


class Board:
    dab_attempt = 0
    score = 0

    def __init__(self, board: list[list[Cell]]) -> None:
        self.board = board

    def try_dab(self, draw_num: str) -> None:
        for i in range(5):
            for x in range(5):
                if self.board[i][x].number == draw_num:
                    self.board[i][x].is_dabbed = True
        self.dab_attempt += 1

    def _is_row_solved(self) -> bool:
        for i in range(5):
            row_check = 0
            for x in range(5):
                if self.board[i][x].is_dabbed:
                    row_check += 1
            if row_check == 5:
                return True
        return False

    def _is_col_solved(self) -> bool:
        for x in range(5):
            col_check = 0
            for i in range(5):
                if self.board[i][x].is_dabbed:
                    col_check += 1
            if col_check == 5:
                return True
        return False

    def is_solved(self) -> bool:
        row_solved = self._is_row_solved()
        col_solved = self._is_col_solved()

        return row_solved or col_solved

    def get_num_attempted_dabs(self) -> int:
        return self.dab_attempt

    def get_board_score(self) -> int:
        self.score = 0
        for i in range(5):
            for x in range(5):
                if not self.board[i][x].is_dabbed:
                    self.score += int(self.board[i][x].number)
        return self.score


def get_board(board_data: list, board_number: int) -> list[list[Cell]]:
    board = []
    board_start = board_number * 6 + 2
    grab_single_board = board_data[board_start : board_start + 5]
    for row_string in grab_single_board:
        row = row_string.split()
        row_cell = [Cell(x) for x in row]
        board.append(row_cell)
    return board


def find_winning_board(boards, number_of_boards: int, draw_numbers: list[str]):
    for draw in draw_numbers:
        for x in range(number_of_boards):
            boards[x].try_dab(draw)
            if boards[x].is_solved():
                score = boards[x].get_board_score() * int(draw)
                return score


def find_losing_board(boards, number_of_boards: int, draw_numbers: list[str]):
    for draw in draw_numbers:
        for x in range(number_of_boards):
            if not boards[x].is_solved():
                boards[x].try_dab(draw)
                score = boards[x].get_board_score() * int(draw)
    return score


for i in range(number_of_boards):
    board_list.append(Board(get_board(data, i)))

solution = find_winning_board(board_list, number_of_boards, draw_numbers)
print(solution)

solution2 = find_losing_board(board_list, number_of_boards, draw_numbers)
print(solution2)
