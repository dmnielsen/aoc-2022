from pathlib import Path

from aoc2022 import AOC_DIR
from aoc2022.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202225_input.txt'


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def snafu2decimal(text: str) -> int:
    total = 0
    for i, num in enumerate(reversed(text)):
        base5 = 5**i
        if str.isnumeric(num):
            total += base5 * int(num)
        elif num == '-':
            total += base5 * -1
        elif num == '=':
            total += base5 * -2
    return total


def decimal2snafu(num: int) -> str:
    remainders = [divmod(num, 5)]
    while remainders[-1][0] > 0:
        remainders.append(divmod(remainders[-1][0], 5))

    snafu = ''
    carry = 0
    for _, r in remainders:
        r += carry
        carry = 0
        if r >= 5:
            r = 0
            carry = 1
        if r == 3:
            carry = 1
            snafu = '=' + snafu
        elif r == 4:
            carry = 1
            snafu = '-' + snafu
        else:
            snafu = str(r) + snafu
    if carry:
        snafu = str(carry) + snafu
    return snafu


def solve_part1(input_: str):
    lines = input_.split('\n')
    total = sum(snafu2decimal(n) for n in lines)

    return decimal2snafu(total)


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)

    if show_solution:
        print_solutions(result1, None)


if __name__ == '__main__':
    main()
