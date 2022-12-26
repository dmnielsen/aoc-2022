from collections import deque
from pathlib import Path
from typing import NamedTuple, Optional

from aoc2022 import AOC_DIR
from aoc2022.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202224_input.txt'


class Coords(NamedTuple):
    row: int
    col: int


Blizzards = dict[str, list[Coords]]

Spaces = set[Coords]


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_input(text: str) -> tuple[Blizzards, Spaces, Spaces]:
    lines = text.strip().split('\n')

    blizzards: Blizzards = {'>': [], '<': [], '^': [], 'v': []}
    empty_spaces = []
    grid = []
    for row, line in enumerate(lines[1:-1]):
        for col, dir in enumerate(line[1:-1]):
            coords = Coords(row, col)
            grid.append(coords)
            if dir == '.':
                empty_spaces.append(coords)
            else:
                blizzards[dir].append(coords)
    return blizzards, set(empty_spaces), set(grid)


def move_blizzards(blizzards: Blizzards, max_row: int, max_col: int) -> Blizzards:
    blizzards['^'] = [Coords(b.row - 1, b.col) if (b.row - 1) >= 0 else Coords(max_row, b.col) for b in blizzards['^']]
    blizzards['v'] = [Coords(b.row + 1, b.col) if (b.row + 1) <= max_row else Coords(0, b.col) for b in blizzards['v']]
    blizzards['>'] = [Coords(b.row, b.col + 1) if (b.col + 1) <= max_col else Coords(b.row, 0) for b in blizzards['>']]
    blizzards['<'] = [Coords(b.row, b.col - 1) if (b.col - 1) >= 0 else Coords(b.row, max_col) for b in blizzards['<']]

    return blizzards


def get_empty_spaces(blizzards: Blizzards, grid: Spaces) -> Spaces:
    filled_spaces = set()
    for key in blizzards.keys():
        filled_spaces.update(blizzards[key])

    return grid - filled_spaces


def valid_moves(loc: Coords, empty_spaces: Spaces) -> Spaces:
    row, col = loc
    possible_moves = {Coords(row + 1, col), Coords(row - 1, col), Coords(row, col + 1), Coords(row, col - 1), loc}

    return possible_moves & empty_spaces


def find_path(
    t: int,
    start: Coords,
    end: Coords,
    blizzard_snapshot: dict[int, Blizzards],
    empty_space_snapshot: dict[int, Spaces],
    grid: Spaces,
):
    max_row = max(g.row for g in grid)
    max_col = max(g.col for g in grid)

    processed: set[tuple[int, Coords]] = set()
    unprocessed: deque[tuple[int, Coords]] = deque([(t, start)])

    while unprocessed:
        t, loc = unprocessed.popleft()
        processed.update([(t, loc)])
        blizzard = blizzard_snapshot.get(t + 1, None)
        if blizzard is None:
            blizzard = blizzard_snapshot[t + 1] = move_blizzards(blizzard_snapshot[t], max_row, max_col)
        empty_spaces = empty_space_snapshot.get(t + 1, None)
        if empty_spaces is None:
            empty_spaces = empty_space_snapshot[t + 1] = get_empty_spaces(blizzard, grid)
            empty_spaces.update([start, end])

        options = valid_moves(loc, empty_spaces)
        for option in options:
            if option.row == end.row and option.col == end.col:
                return t + 1
            if (t + 1, option) not in processed and (t + 1, option) not in unprocessed:
                unprocessed.append((t + 1, option))


def solve_part1(input_: str):

    initial_blizzards, empty_spaces, grid = parse_input(input_)
    max_row = max(g.row for g in grid)
    max_col = max(g.col for g in grid)

    blizzard_snapshot = {0: initial_blizzards}
    empty_space_snapshot = {0: empty_spaces}

    start = Coords(-1, 0)
    end = Coords(max_row + 1, max_col)

    return find_path(0, start, end, blizzard_snapshot, empty_space_snapshot, grid)


def solve_part2(input_: str):
    initial_blizzards, empty_spaces, grid = parse_input(input_)
    max_row = max(g.row for g in grid)
    max_col = max(g.col for g in grid)

    blizzard_snapshot = {0: initial_blizzards}
    empty_space_snapshot = {0: empty_spaces}

    start = Coords(-1, 0)
    end = Coords(max_row + 1, max_col)

    # Find path to end
    steps_to_end = find_path(0, start, end, blizzard_snapshot, empty_space_snapshot, grid)
    print(f'Steps to end: {steps_to_end}')

    # Find path back
    steps_to_start = find_path(steps_to_end, end, start, blizzard_snapshot, empty_space_snapshot, grid)
    print(f'Steps to start: {steps_to_start}')

    # And back again
    steps_to_end_redux = find_path(steps_to_start, start, end, blizzard_snapshot, empty_space_snapshot, grid)

    return steps_to_end_redux


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
