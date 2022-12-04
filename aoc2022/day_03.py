import string
from itertools import islice
from pathlib import Path
from typing import Dict, Iterable, List

from aoc2022 import AOC_DIR
from aoc2022.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202203_input.txt'


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_input(text: str) -> List[str]:
    return text.strip().split('\n')


def generate_priority_dict() -> Dict[str, int]:
    lower = {l: ind for ind, l in enumerate(string.ascii_lowercase, start=1)}
    upper = {l: ind for ind, l in enumerate(string.ascii_uppercase, start=27)}
    return lower | upper


def find_common_item(text: str) -> str:

    if len(text) // 2 == 1:
        print('odd')
    mid_idx = len(text) // 2

    left = text[:mid_idx]
    right = text[mid_idx:]

    return (set(left) & set(right)).pop()


def find_badge_item(elf1: str, elf2: str, elf3: str) -> str:

    return (set(elf1) & set(elf2) & set(elf3)).pop()


def batched(iterable: Iterable[str], n: int) -> Iterable:
    """Batch data into lists of length n. The last batch may be shorter.

    Nicked from itertools recipes

    Example
    -------
    > batched('ABCDEFG', 3) --> ABC DEF G
    """
    #
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while batch := list(islice(it, n)):
        yield batch


def solve_part1(input_: str) -> int:
    priority_val = generate_priority_dict()
    rucksacks = parse_input(input_)

    common_item_priorities = [priority_val[find_common_item(rucksack)] for rucksack in rucksacks]

    return sum(common_item_priorities)


def solve_part2(input_: str) -> int:
    priority_val = generate_priority_dict()
    rucksacks = parse_input(input_)

    badges = [priority_val[find_badge_item(*items)] for items in batched(rucksacks, 3)]

    return sum(badges)


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
