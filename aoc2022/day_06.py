import collections
from itertools import islice
from pathlib import Path
from typing import Iterable

from aoc2022 import AOC_DIR
from aoc2022.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202206_input.txt'


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def sliding_window(iterable: Iterable, n: int) -> tuple[str]:
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def solve_part1(input_: str) -> int:
    for i, window in enumerate(sliding_window(input_.strip(), 4)):
        idx = 4 + i
        if len(set(window)) == 4:
            break
    return idx


def solve_part2(input_: str) -> int:
    for i, window in enumerate(sliding_window(input_.strip(), 14)):
        idx = 14 + i
        if len(set(window)) == 14:
            break
    return idx


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
