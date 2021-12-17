from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=1)
data = puzzle.input_data.splitlines()
int_data = list(map(int, data))


def max_increase(measurements):
    previous_measurment = measurements[0]
    num_of_increase = 0

    for measurement in measurements:

        if measurement > previous_measurment:
            num_of_increase += 1

        previous_measurment = measurement
    return num_of_increase


def sliding_window(measurments):
    arr_length = len(measurments)
    window_size = 3
    window_sum1 = sum(measurments[:window_size])
    window_sum2 = window_sum1
    increase_total = 0

    for i in range(arr_length - window_size):
        window_sum2 = window_sum2 - measurments[i] + measurments[i + window_size]
        if window_sum2 > window_sum1:
            increase_total += 1
        window_sum1 = window_sum2
    return increase_total


solution = max_increase(int_data)
print(solution)
solution2 = sliding_window(int_data)
print(solution2)
