from collections import deque
from pathlib import Path

from aoc2022 import AOC_DIR
from aoc2022.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202205_input.txt'


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_instructions(text: str) -> list[tuple]:
    """Returns move instructions as tuple

    Note: stack numbers are re-indexed to zero
    """
    instructions = []
    for instruction in text.strip().split('\n'):
        line = instruction.split(' ')
        instructions.append((int(line[1]), int(line[3]) - 1, int(line[5]) - 1))
    return instructions


def parse_stack(text: str, return_stack: bool = True) -> list:
    text = text.split('\n')
    n_stacks = int(max(text[-1].split()))

    stacks = ['' for _ in range(n_stacks)]

    for line in text[:-1]:
        stacks = [stack + line[n * 4 + 1] for n, stack in enumerate(stacks)]

    if return_stack:
        return [deque(char for char in stack.lstrip()[::-1]) for stack in stacks]
    else:
        return [[char for char in stack.lstrip()[::-1]] for stack in stacks]


def parse_data(text: str, part2: bool = False):
    stack_info, raw_instructions = text.split('\n\n')

    instructions = parse_instructions(raw_instructions)
    stacks = parse_stack(stack_info, part2)
    return stacks, instructions


def solve_part1(input_: str):
    stacks, instructions = parse_data(input_)
    for number, start, end in instructions:
        for _ in range(number):
            stacks[end].append(stacks[start].pop())

    top = ''.join([stack.pop() for stack in stacks])

    return top


def solve_part2(input_: str):
    stacks, instructions = parse_data(input_, False)
    for number, start, end in instructions:
        stacks[end].extend(stacks[start][-number:])
        del stacks[start][-number:]

    top = ''.join([stack.pop() for stack in stacks])

    return top


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
