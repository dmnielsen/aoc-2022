import re
from pathlib import Path
from typing import Sequence

from aoc2022 import AOC_DIR
from aoc2022.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202222_input.txt'


clockwise = {'U': 'R', 'R': 'D', 'D': 'L', 'L': 'U'}

counterclockwise = {'U': 'L', 'L': 'D', 'D': 'R', 'R': 'U'}


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_input(text: str) -> tuple[list[str], str]:
    path, directions = text.split('\n\n')

    lines = path.split('\n')
    max_width = max(len(row) for row in lines)

    rows = []
    for line in lines:
        rows.append(f"{line:<{max_width}}")
    return rows, directions.strip()


def parse_directions(text: str) -> list[tuple[str, str]]:
    p = re.compile(r'(\d*)([RL])')
    steps = p.findall(text)
    last_step = text[text.rindex(steps[-1][-1]) + 1 :]
    steps.append((last_step,))
    return steps


def move_right(loc: tuple[int, int], steps: int, grid: list[str]) -> tuple[int, int]:
    for i in range(steps):
        row, idx = loc[0], loc[1] + 1
        if idx == len(grid[row]):
            idx = 0
        ahead = grid[row][idx]
        if ahead == ' ':
            while ahead == ' ':
                idx = idx + 1
                if idx == len(grid[row]):
                    idx = 0
                ahead = grid[row][idx]
        if ahead == '#':
            return loc
        else:
            loc = (row, idx)
    return loc


def move_left(loc: tuple[int, int], steps: int, grid: list[str]) -> tuple[int, int]:
    for i in range(steps):
        row, idx = loc[0], loc[1] - 1
        if idx == -1:
            idx = len(grid[row]) - 1
        ahead = grid[row][idx]
        if ahead == ' ':
            while ahead == ' ':
                idx = idx - 1
                if idx == -1:
                    idx = len(grid[row]) - 1
                ahead = grid[row][idx]
        if ahead == '#':
            return loc
        else:
            loc = (row, idx)
    return loc


def move_down(loc: tuple[int, int], steps: int, grid: list[str]) -> tuple[int, int]:
    for i in range(steps):
        row, idx = loc[0] + 1, loc[1]
        if row == len(grid):
            row = 0
        ahead = grid[row][idx]
        if ahead == ' ':
            while ahead == ' ':
                row += 1
                if row == len(grid):
                    row = 0
                ahead = grid[row][idx]
        if ahead == '#':
            return loc
        else:
            loc = (row, idx)
    return loc


def move_up(loc: tuple[int, int], steps: int, grid: list[str]) -> tuple[int, int]:
    for i in range(steps):
        row, idx = loc[0] - 1, loc[1]
        if row < 0:
            row = len(grid) - 1
        ahead = grid[row][idx]
        if ahead == ' ':
            while ahead == ' ':
                row -= 1
                if row < 0:
                    row = len(grid) - 1
                ahead = grid[row][idx]
        if ahead == '#':
            return loc
        else:
            loc = (row, idx)
    return loc


def follow_directions(path: list[str], directions: list[tuple[str, str]]) -> tuple[tuple[int, int], str]:
    heading_func = {'R': move_right, 'L': move_left, 'U': move_up, 'D': move_down}

    heading = 'R'
    loc = (0, path[0].index('.'))

    for steps_turn in directions:
        try:
            steps, turn = steps_turn
        except ValueError:
            steps = steps_turn[0]
            turn = None

        loc = heading_func[heading](loc, int(steps), path)

        if turn is None:
            return loc, heading
        elif turn == 'R':
            heading = clockwise[heading]
        elif turn == 'L':
            heading = counterclockwise[heading]
    return loc, heading


def calculate_password(loc: tuple[int, int], heading: str) -> int:
    heading_values = {'R': 0, 'D': 1, 'L': 2, 'U': 3}
    return 1000 * (loc[0] + 1) + 4 * (loc[1] + 1) + heading_values[heading]


def solve_part1(input_: str) -> int:
    path, raw_directions = parse_input(input_)
    directions = parse_directions(raw_directions)

    loc, heading = follow_directions(path, directions)

    return calculate_password(loc, heading)


def generate_wrap_instructions() -> dict[tuple[int, int], tuple[tuple[int, int], str]]:
    #    row    col
    # A: [0:50][50:100]
    # B: [0:50][100:150]
    # C: [50:100][50:100]
    # D: [100:150][50:100]
    # E: [100:150][0:50]
    # F: [150:200][0:50]

    wrap = {}

    # wrap A UP / wrap F LEFT
    for col in range(50, 100):
        wrap[(-1, col)] = ((150 + col - 50, 0), 'R')
        wrap[(150 + col - 50, -1)] = ((0, col), 'D')
    # wrap A LEFT / wrap E LEFT
    for row in range(0, 50):
        wrap[(row, 49)] = ((149 - row, 0), 'R')
        wrap[(149 - row, -1)] = ((row, 50), 'R')
    # wrap B UP / wrap F DOWN and wrap B DOWN / wrap C RIGHT
    for col in range(100, 150):
        wrap[(-1, col)] = ((199, col - 100), 'U')
        wrap[(200, col - 100)] = ((0, col), 'D')

        wrap[(50, col)] = ((col - 50, 99), 'L')
        wrap[(col - 50, 100)] = ((49, col), 'U')
    # wrap B RIGHT / wrap D RIGHT
    for row in range(0, 50):
        wrap[(row, 150)] = ((49 - row + 100, 99), 'L')
        wrap[(49 - row + 100, 100)] = ((row, 149), 'L')
    # wrap C LEFT / wrap E UP
    for row in range(50, 100):
        wrap[(row, 49)] = ((100, row - 50), 'D')
        wrap[(99, row - 50)] = ((row, 50), 'R')
    # wrap D DOWN / wrap F RIGHT
    for col in range(50, 100):
        wrap[(150, col)] = ((150 + col - 50, 49), 'L')
        wrap[(150 + col - 50, 50)] = ((149, col), 'U')

    return wrap


def generate_test_wrap_instructions() -> dict[tuple[int, int], tuple[tuple[int, int], str]]:
    wrap = {}

    # side 1 UP / side 2 UP
    for col in range(8, 12):
        wrap[(-1, col)] = ((4, col - 8), 'D')
        wrap[(3, col - 8)] = ((0, col), 'D')
    # side 1 LEFT / side 3 UP and side 1 RIGHT / side 6 RIGHT
    for row in range(0, 4):
        # breakpoint()
        wrap[(row, 7)] = ((4, 4 + row), 'D')
        wrap[(3, 4 + row)] = ((row, 8), 'R')
        wrap[(row, 12)] = ((8 + 3 - row, 15), 'L')
        wrap[(8 + 3 - row, 16)] = ((row, 11), 'L')
    # side 2 DOWN / side 5 DOWN
    for col in range(0, 4):
        wrap[(8, col)] = ((11, 8 + 3 - col), 'U')
        wrap[(12, 8 + 3 - col)] = ((7, col), 'U')
    # side 2 LEFT / side 6 DOWN
    for row in range(4, 8):
        wrap[(row, -1)] = ((12 + 7 - row, 11), 'U')
        wrap[(12 + 7 - row, 12)] = ((row, 0), 'R')
    # side 3 DOWN / side 5 LEFT
    for col in range(4, 8):
        wrap[(8, col)] = ((8 + 7 - col, 8), 'R')
        wrap[(8 + 7 - col, 7)] = ((7, col), 'U')
    # side 4 RIGHT / side 6 UP
    for row in range(4, 8):
        wrap[(row, 12)] = ((8, 12 + 7 - row), 'D')
        wrap[(7, 12 + 7 - row)] = ((row, 11), 'L')

    return wrap


def follow_directions_cube(
    path: list[str],
    directions: list[tuple[str, str]],
    wrap_instruction: dict[tuple[int, int], tuple[tuple[int, int], str]],
) -> tuple[tuple[int, int], str]:

    heading = 'R'
    loc = (0, path[0].index('.'))

    for steps_turn in directions:
        next_heading = heading

        try:
            steps, turn = steps_turn
        except ValueError:
            steps = steps_turn[0]
            turn = None

        for _ in range(int(steps)):
            row, col = loc
            if heading == 'R':
                col += 1
            elif heading == 'L':
                col -= 1
            elif heading == 'U':
                row -= 1
            elif heading == 'D':
                row += 1

            try:
                ahead = path[row][col]
            except IndexError:
                next_loc, next_heading = wrap_instruction[(row, col)]
                row, col = next_loc
                ahead = path[row][col]
            if ahead == ' ':
                next_loc, next_heading = wrap_instruction[(row, col)]
                row, col = next_loc
                ahead = path[row][col]

            if ahead == '#':
                break
            else:
                loc = (row, col)
                heading = next_heading

        if turn is None:
            return loc, heading
        elif turn == 'R':
            heading = clockwise[heading]
        elif turn == 'L':
            heading = counterclockwise[heading]
    return loc, heading


def solve_part2(input_: str, test: bool = False) -> int:
    path, raw_directions = parse_input(input_)
    directions = parse_directions(raw_directions)

    if test:
        wrap_instructions = generate_test_wrap_instructions()
    else:
        wrap_instructions = generate_wrap_instructions()

    loc, heading = follow_directions_cube(path, directions, wrap_instructions)

    return calculate_password(loc, heading)


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
