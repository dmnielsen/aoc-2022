from pathlib import Path

from typing import List

from aoc2022 import AOC_DIR
from aoc2022.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202201_input.txt'


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_file(text: str) -> List[List[int]]:
    """Return list of elves' inventory lists"""
    return [[int(cals) for cals in elf.split()] for elf in text.split('\n\n')]


def solve_part1(input_: str) -> int:
    elf_inventories = parse_file(input_)
    return max([sum(inventory) for inventory in elf_inventories])


def solve_part2(input_: str) -> int:
    elf_inventories = parse_file(input_)
    return sum(sorted([sum(inventory) for inventory in elf_inventories], reverse=True)[:3])


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
