from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=2)
data = puzzle.input_data.splitlines()


def sub_destination(route: list[str]):
    y_axis = 0
    x_axis = 0
    aim = 0
    hor_axis = 0

    format_directions = [x.split(" ") for x in route]
    directions = [(x,int(y))for (x,y) in format_directions]
    for direction in directions:
        match direction:
            case ('forward', amount):
                x_axis = x_axis + amount
                hor_axis = hor_axis + (aim*amount)
            case('up', amount):
                y_axis = y_axis - amount
                aim = aim - amount
            case ('down', amount):
                y_axis = y_axis + amount
                aim = aim + amount

    destination1 = x_axis * y_axis
    destination2 = x_axis * hor_axis

    return destination1, destination2


solution1 = sub_destination(data)
print(solution1)
