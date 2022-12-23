from collections import Counter
from pathlib import Path
from typing import Callable, NamedTuple, Optional

from aoc2022 import AOC_DIR
from aoc2022.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202223_input.txt'


class Coords(NamedTuple):
    x: int
    y: int


class Positions(NamedTuple):
    N: Coords
    S: Coords
    E: Coords
    W: Coords
    NE: Coords
    NW: Coords
    SE: Coords
    SW: Coords


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_input(text: str) -> set[Coords]:
    elves = set()

    lines = text.strip().split('\n')
    for y, line in enumerate(lines[::-1]):
        for x, char in enumerate(line):
            if char == '#':
                elves.update([Coords(x, y)])
    return elves


def adjacent_coords(coords: Coords) -> Positions:

    x, y = coords
    return Positions(
        N=Coords(x, y + 1),
        S=Coords(x, y - 1),
        E=Coords(x + 1, y),
        W=Coords(x - 1, y),
        NE=Coords(x + 1, y + 1),
        NW=Coords(x - 1, y + 1),
        SE=Coords(x + 1, y - 1),
        SW=Coords(x - 1, y - 1),
    )


def go_north(elf: Coords, options: Positions, others: set[Coords]) -> Optional[Coords]:
    if len({options.N, options.NW, options.NE} - others) == 3:
        return Coords(elf.x, elf.y + 1)
    return None


def go_south(elf: Coords, options: Positions, others: set[Coords]) -> Optional[Coords]:
    if len({options.S, options.SW, options.SE} - others) == 3:
        return Coords(elf.x, elf.y - 1)
    return None


def go_east(elf: Coords, options: Positions, others: set[Coords]) -> Optional[Coords]:
    if len({options.E, options.SE, options.NE} - others) == 3:
        return Coords(elf.x + 1, elf.y)
    return None


def go_west(elf: Coords, options: Positions, others: set[Coords]) -> Optional[Coords]:
    if len({options.W, options.NW, options.SW} - others) == 3:
        return Coords(elf.x - 1, elf.y)
    return None


def proposed_position(elf: Coords, other_elves: set[Coords], order: list[Callable]) -> Optional[Coords]:
    adjacent = adjacent_coords(elf)
    if all(coords not in other_elves for coords in adjacent):
        return None
    for direction in order:
        proposal = direction(elf, adjacent, other_elves)
        if proposal is not None:
            return proposal
    return None


def propose_moves(elves: set[Coords], order: list[Callable]) -> dict[Coords, Coords]:
    elf_proposals = {}
    for elf in elves:
        position = proposed_position(elf, elves, order)
        if position is not None:
            elf_proposals[elf] = position
    return elf_proposals


def check_and_move(elves: set[Coords], proposals: dict[Coords, Coords]) -> set[Coords]:
    count_locs = Counter(proposals.values())
    unavailable = {loc for loc, count in count_locs.items() if count > 1}

    for current, proposed in proposals.items():
        if proposed in unavailable:
            continue
        elves.remove(current)
        elves.update([proposed])
    return elves


def get_rectangle_size(elves: set[Coords]) -> tuple[int, int, int, int]:
    min_x, *_, max_x = sorted([c.x for c in elves])
    min_y, *_, max_y = sorted([c.y for c in elves])
    return min_x, max_x, min_y, max_y


def find_empties(elves: set[Coords]) -> set[Coords]:
    min_x, *_, max_x = sorted([c.x for c in elves])
    min_y, *_, max_y = sorted([c.y for c in elves])
    rectangle = []
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            rectangle.append(Coords(x, y))
    return set(rectangle) - elves


def print_positions(elves: set[Coords]) -> str:
    position_str = []
    x1, x2, y1, y2 = get_rectangle_size(elves)

    for y in range(y2, y1 - 1, -1):

        row = ''
        for x in range(x1, x2 + 1):
            if Coords(x, y) in elves:
                row += '#'
            else:
                row += '.'
        position_str.append(row)
    return '\n'.join(position_str)


def solve_part1(input_: str) -> int:
    elves = parse_input(input_)

    order_of_preference = [go_north, go_south, go_west, go_east]

    for i in range(10):
        proposals = propose_moves(elves, order_of_preference)
        elves = check_and_move(elves, proposals)

        move_to_end = order_of_preference.pop(0)
        order_of_preference.append(move_to_end)

    return len(find_empties(elves))


def solve_part2(input_: str) -> int:
    elves = parse_input(input_)

    last_position = print_positions(elves)
    current_position = ''

    order_of_preference = [go_north, go_south, go_west, go_east]

    i = 0
    while last_position != current_position:
        last_position = current_position
        proposals = propose_moves(elves, order_of_preference)
        elves = check_and_move(elves, proposals)

        current_position = print_positions(elves)

        move_to_end = order_of_preference.pop(0)
        order_of_preference.append(move_to_end)

        i += 1

    return i


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
