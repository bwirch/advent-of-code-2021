from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=3)
data = puzzle.input_data.splitlines()


def get_power_consumption(binary_list):
    digit_totals = []
    for digit in binary_list[0]:
        digit_totals.append([0, 0])

    for binary_number in binary_list:
        i = 0
        for digit in binary_number:
            digit_totals[i][int(digit)] += 1
            i += 1

    gamma = ""
    epsilon = ""
    for x in digit_totals:
        if x[0] > x[1]:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    power_consumption = int(gamma, 2) * int(epsilon, 2)

    return digit_totals, power_consumption


def get_ratings(binary_list):
    working_list = []
    next_list = binary_list
    i = len(binary_list[0])

    for digit in range(i):
        digit_total = [0, 0]
        for binary_number in next_list:
            digit_total[int(binary_number[digit])] += 1
        print(digit_total)
        if digit_total[0] > digit_total[1]:
            for number in next_list:
                if number[digit] == 0:
                    working_list.append(number)
        elif digit_total[1] >= digit_total[0]:
            for number in next_list:
                if number[digit] == 1:
                    working_list.append(number)
        print(working_list)
        next_list = working_list
        working_list = []
        if len(next_list) == 1:
            break
    return next_list


solution1 = get_power_consumption(data)
# print(solution1)
solution2 = get_ratings(data)
print(solution2)
