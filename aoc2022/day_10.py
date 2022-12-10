from pathlib import Path

from aoc2022 import AOC_DIR
from aoc2022.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202210_input.txt'


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_instructions(text: str) -> dict[int, int]:
    cycle = 1
    X = 1
    signal_strengths = {}
    for line in (lines := text.strip().split('\n')):
        if line == 'noop':
            signal_strengths[cycle] = X
            cycle += 1
        else:
            _, value = line.split(' ')
            signal_strengths[cycle] = X
            cycle += 1
            signal_strengths[cycle] = X
            cycle += 1
            X += int(value)
    if not lines[-1] == 'noop':
        signal_strengths[cycle] = X
    return signal_strengths


def calculate_signal_strength(cycle: int, value: int) -> int:
    return cycle * value


def solve_part1(input_: str) -> int:
    signal_strengths = parse_instructions(input_)
    sum_of_strengths = 0
    cycles = [20, 60, 100, 140, 180, 220]

    for cycle in cycles:
        sum_of_strengths += calculate_signal_strength(cycle, signal_strengths[cycle])

    return sum_of_strengths


def solve_part2(input_: str, fill: str = '█', space: str = ' ') -> str:
    signal_strengths = parse_instructions(input_)

    image = ''
    for crt_loc in range(240):
        cycle = crt_loc + 1
        if crt_loc % 40 == 0:
            image += '\n'
        sprite = signal_strengths[cycle]
        if (sprite - (crt_loc % 40)) in (-1, 0, 1):
            image += fill
        else:
            image += space
    print(image)
    return image


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
