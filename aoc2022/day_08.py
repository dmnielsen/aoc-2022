from pathlib import Path
from typing import Generator, Iterable

import numpy as np

from aoc2022 import AOC_DIR
from aoc2022.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202208_input.txt'


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_grid(text: str) -> np.ndarray:
    return np.array([[int(char) for char in line] for line in text.strip().split('\n')])


def is_visible(tree_height: int, line_of_sight: np.ndarray) -> bool:
    return all(line_of_sight < tree_height)


def count_visible_trees(tree_grid: np.ndarray) -> int:
    max_i, max_j = tree_grid.shape

    visible_trees = 0
    for i in range(max_i):
        for j in range(max_j):
            if i == 0 or i == (max_i - 1):
                visible_trees += 1
            elif j == 0 or j == (max_j - 1):
                visible_trees += 1
            else:
                top_los = tree_grid[:i, j]
                bottom_los = tree_grid[-1:i:-1, j]
                left_los = tree_grid[i, :j]
                right_los = tree_grid[i, -1:j:-1]

                lines_of_sight = [top_los, bottom_los, left_los, right_los]

                if any(is_visible(tree_grid[i, j], los) for los in lines_of_sight):
                    visible_trees += 1
    return visible_trees


def yield_shorter_trees_in_los(iterable: Iterable, tree_height: int) -> Generator:
    it = iter(iterable)
    for x in it:
        if x >= tree_height:
            yield x
            break
        else:
            yield x


def calculate_scenic_score(tree_loc: tuple[int, int], grid: np.ndarray) -> int:
    i, j = tree_loc
    tree_height = grid[i, j]

    top = yield_shorter_trees_in_los(grid[i - 1 :: -1, j], tree_height)
    bottom = yield_shorter_trees_in_los(grid[i + 1 :, j], tree_height)
    left = yield_shorter_trees_in_los(grid[i, j - 1 :: -1], tree_height)
    right = yield_shorter_trees_in_los(grid[i, j + 1 :], tree_height)

    return len(list(top)) * len(list(bottom)) * len(list(left)) * len(list(right))


def solve_part1(input_: str) -> int:
    grid = parse_grid(input_)
    return count_visible_trees(grid)


def solve_part2(input_: str) -> int:
    grid = parse_grid(input_)
    max_i, max_j = grid.shape

    max_scenic_score = 0

    for i in range(1, max_i - 1):
        for j in range(1, max_j - 1):
            score = calculate_scenic_score((i, j), grid)
            if score > max_scenic_score:
                max_scenic_score = score
    return max_scenic_score


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
