from pathlib import Path

from typing import Tuple

from aoc2022 import AOC_DIR
from aoc2022.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202204_input.txt'


Section = Tuple[int, int]


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_data(text: str) -> list[tuple[Section, Section]]:
    assignments = []
    for line in text.strip().split('\n'):
        left, right = line.split(',')
        left = tuple(int(num) for num in left.split('-'))
        right = tuple(int(num) for num in right.split('-'))
        assignments.append((left, right))
    return assignments


def is_fully_contained(section: Section, range: Section) -> bool:
    if section[0] >= range[0] and section[1] <= range[1]:
        return True
    else:
        return False


def any_overlap(section: Section, range: Section) -> bool:
    if range[0] <= section[0] <= range[1]:
        return True
    elif range[0] <= section[1] <= range[1]:
        return True
    else:
        return False


def solve_part1(input_: str) -> int:
    assignments = parse_data(input_)

    fully_contained_assignments = 0
    for elf1, elf2 in assignments:
        if is_fully_contained(elf1, elf2):
            fully_contained_assignments += 1
        elif is_fully_contained(elf2, elf1):
            fully_contained_assignments += 1
        else:
            continue
    return fully_contained_assignments


def solve_part2(input_: str) -> int:
    assignments = parse_data(input_)

    overlaps = 0
    for elf1, elf2 in assignments:
        if any_overlap(elf1, elf2):
            overlaps += 1
        elif any_overlap(elf2, elf1):
            overlaps += 1
    return overlaps


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
