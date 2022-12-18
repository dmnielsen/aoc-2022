from itertools import zip_longest
from pathlib import Path
from typing import Any, Optional

from aoc2022 import AOC_DIR
from aoc2022.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202213_input.txt'


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_input(text: str) -> list:
    pairs = text.strip().split('\n\n')

    list_of_pairs = []
    for pair in pairs:
        left, right = pair.split('\n')
        list_of_pairs.append((eval(left), eval(right)))
    return list_of_pairs


def is_right_order(left_packet, right_packet) -> Any:
    """Return true if in right order; false if not in right order;
    returns None if full list passes without triggering ordering rules"""

    for left, right in zip_longest(left_packet, right_packet, fillvalue=None):
        if left is None:
            return True
        elif right is None:
            return False
        # Both are lists, pass the lists to is_right_order
        elif isinstance(left, list) and isinstance(right, list):
            inner = is_right_order(left, right)
            if inner is not None:
                return inner
        elif isinstance(left, int) and isinstance(right, int):
            if right < left:
                return False
            if left < right:
                return True
        elif isinstance(left, list) and isinstance(right, int):
            inner = is_right_order(left, [right])
            if inner is not None:
                return inner
        elif isinstance(left, int) and isinstance(right, list):
            inner = is_right_order([left], right)
            if inner is not None:
                return inner
        else:
            print('problem')
            return None


def parse_input_part2(text: str) -> list:
    lines = text.strip().split()

    packets = []
    for line in lines:
        packets.append(eval(line))
    return packets


def solve_part1(input_: str) -> int:
    pairs = parse_input(input_)

    index_of_ordered_pairs = 0
    for i, pair in enumerate(pairs, start=1):
        if is_right_order(*pair):
            index_of_ordered_pairs += i

    return index_of_ordered_pairs


def solve_part2(input_: str) -> int:
    divider_packets = [[[2]], [[6]]]

    packets = parse_input_part2(input_)
    packets.extend(divider_packets)

    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(packets)):
            for j in range(len(packets) - i - 1):
                if not is_right_order(packets[j], packets[j + 1]):
                    is_sorted = False
                    insert_packet = packets.pop(j + 1)
                    packets.insert(j, insert_packet)

    decoder_key = []
    for i, packet in enumerate(packets, start=1):
        if (packet == [[2]]) or (packet == [[6]]):
            decoder_key.append(i)
    return decoder_key[0] * decoder_key[1]


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
