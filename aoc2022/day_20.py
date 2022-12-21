from copy import copy
from pathlib import Path
from typing import Optional, cast

from aoc2022 import AOC_DIR
from aoc2022.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202220_input.txt'


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_input(text: str) -> dict[int, int]:
    return {i: int(x) for i, x in enumerate(text.strip().split('\n'))}


def move_index(orig_idx: int, value: int, position_list: list[int]):
    position_list = copy(position_list)

    current_idx = position_list.index(orig_idx)
    size = len(position_list)

    move = value % (size - 1)
    new_index = (current_idx + move) % (size - 1)

    if new_index == 0:
        new_index = size - 1
    position_list.remove(orig_idx)
    position_list.insert(new_index, orig_idx)

    return position_list


def mix_list(number_dict: dict[int, int], position_list: Optional[list[int]] = None) -> list[int]:
    """Returns position list"""
    if not position_list:
        positions = list(number_dict.keys())
    else:
        positions = position_list

    for key, value in number_dict.items():
        positions = move_index(key, value, positions)

    return positions


def get_coords(num_list: list[int], zero_index: int) -> int:
    size = len(num_list)
    return (
        num_list[(zero_index + 1000) % size]
        + num_list[(zero_index + 2000) % size]
        + num_list[(zero_index + 3000) % size]
    )


def solve_part1(input_: str):
    number_dict = parse_input(input_)

    position_list = mix_list(number_dict)

    num_list = [number_dict[i] for i in position_list]
    zero_idx = num_list.index(0)
    return get_coords(num_list, zero_idx)


def apply_decryption_key(key: int, number_dict: dict[int, int]) -> dict[int, int]:
    return {i: v * key for i, v in number_dict.items()}


def solve_part2(input_: str):
    number_dict = parse_input(input_)
    decryption_key = 811589153

    updated_number_dict = apply_decryption_key(decryption_key, number_dict)
    position_list: list[int] = []

    for i in range(10):
        position_list = mix_list(updated_number_dict, position_list)

    num_list = [updated_number_dict[i] for i in position_list]
    zero_idx = num_list.index(0)

    return get_coords(num_list, zero_idx)


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)  # guessed 10772
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
