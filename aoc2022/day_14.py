import re
from collections import namedtuple
from math import fabs
from pathlib import Path

from aoc2022 import AOC_DIR
from aoc2022.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202214_input.txt'


Coords = namedtuple('Coords', ['x', 'y'])


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def sign(num: int) -> int:
    return int(num / fabs(num))


def parse_input(text: str) -> dict[Coords, int]:
    p = re.compile(r'(\d+),(\d+)')
    lines = text.strip().split('\n')

    grid = {}

    for line in lines:
        points = p.findall(line)
        points = [[int(val) for val in point] for point in points]
        for start, end in zip(points, points[1:]):
            # breakpoint()
            delta_x = end[0] - start[0]
            delta_y = end[1] - start[1]
            if delta_x:
                y = start[1]
                for x in range(start[0], end[0] + sign(delta_x), sign(delta_x)):
                    grid[Coords(x, y)] = 1
            elif delta_y:
                x = start[0]
                for y in range(start[1], end[1] + sign(delta_y), sign(delta_y)):
                    grid[Coords(x, y)] = 1
            else:
                print(points)

    # add source point:
    grid[Coords(500, 0)] = 1
    x_vals = [point.x for point in grid.keys()]
    x_min, x_max = min(x_vals), max(x_vals)

    y_vals = [point.y for point in grid.keys()]
    y_min, y_max = min(y_vals), max(y_vals)

    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            point = Coords(x, y)
            val = grid.get(point, 0)

            grid[point] = val
    return grid


def vertical_drop(point: Coords) -> Coords:
    return Coords(point.x, point.y + 1)


def left_diagonal_drop(point: Coords) -> Coords:
    return Coords(point.x - 1, point.y + 1)


def right_diagonal_drop(point: Coords) -> Coords:
    return Coords(point.x + 1, point.y + 1)


def drop_grain_of_sand(grid: dict[Coords, int], y_max: int, floor=False):
    current_position = Coords(500, 0)

    while True:
        vertical = vertical_drop(current_position)
        left_diag = left_diagonal_drop(current_position)
        right_diag = right_diagonal_drop(current_position)

        if (current_position == Coords(500, 0)) and (grid[vertical]) and (grid[left_diag]) and (grid[right_diag]):
            return None
        if current_position.y == y_max:
            return None
        if not grid.get(vertical, 0):
            current_position = vertical
            continue
        elif not grid.get(left_diag, 0):
            current_position = left_diag
        elif not grid.get(right_diag, 0):
            current_position = right_diag
        else:
            return current_position


def solve_part1(input_: str) -> int:
    grid = parse_input(input_)
    y_max = max(point.y for point in grid.keys())

    sand_grains = 0
    while True:
        resting_position = drop_grain_of_sand(grid, y_max)
        if resting_position is None:
            return sand_grains
        else:
            grid[resting_position] = 1
            sand_grains += 1


def solve_part2(input_: str) -> int:
    grid = parse_input(input_)
    y_max = max(point.y for point in grid.keys()) + 2
    x_max = max(point.x for point in grid.keys())
    for x in range(0, x_max * 3):
        grid[Coords(x, y_max)] = 1

    sand_grains = 0
    while True:
        resting_position = drop_grain_of_sand(grid, y_max, floor=True)
        if resting_position is None:
            return sand_grains + 1
        else:
            grid[resting_position] = 1
            sand_grains += 1


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
