from collections import deque
from math import floor, lcm
from pathlib import Path

from aoc2022 import AOC_DIR
from aoc2022.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202211_input.txt'


class Monkey:
    def __init__(self, number: int, items: list[int], operation: list[str], test: int, test_true: int, test_false: int):
        self.number = number
        self.operation = operation
        self.operation_func = self.pick_operation()
        self.divisible_by = test
        self.pass_if_true = test_true
        self.pass_if_false = test_false

        self.holding_items = self._initialize_items(items)

        self.items_inspected = 0

    def __repr__(self) -> str:
        return f'Monkey(number={self.number})'

    def __str__(self) -> str:
        return f'Monkey {self.number}: {self.print_items()}'

    @staticmethod
    def _initialize_items(items: list[int]):
        item_list: deque[int] = deque([])
        for item in items:
            item_list.append(item)
        return item_list

    def print_items(self) -> str:
        return ', '.join([str(x) for x in self.holding_items])

    def has_items(self) -> bool:
        if len(self.holding_items):
            return True
        return False

    def inspect_item(self, relief: bool = True, mod: int = 0) -> tuple[int, int]:
        """Inspect item; returns item and monkey number to pass to"""

        self.items_inspected += 1

        item = self.holding_items.popleft()

        item = self.operation_func(item)

        if relief:
            item = floor(item / 3)

        if mod:
            item = item % mod

        if (item % self.divisible_by) == 0:
            return self.pass_if_true, item
        else:
            return self.pass_if_false, item

    def catch_item(self, item):
        self.holding_items.append(item)

    def square_worry(self, worry: int):
        return worry * worry

    def add_worry(self, worry: int):
        return worry + int(self.operation[1])

    def multiply_worry(self, worry: int):
        return worry * int(self.operation[1])

    def pick_operation(self):
        if self.operation[-1] == 'old':
            return self.square_worry
        elif self.operation[0] == '+':
            return self.add_worry
        elif self.operation[0] == '*':
            return self.multiply_worry
        else:
            raise ValueError(f'{self.operation} did not match')


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_items(text: str) -> list[str]:
    idx = text.find(':')
    return text[idx + 2 :].split(', ')


def parse_monkey_text(text: str) -> tuple[int, list[int], list[str], int, int, int]:
    lines: list[str] = text.strip().split('\n')
    number = int(lines[0][-2])
    starting_items = [int(x) for x in parse_items(lines[1])]
    operation = lines[2].strip().split(' ')[-2:]
    test = int(lines[3].strip().split(' ')[-1])
    test_true = int(lines[4].strip().split(' ')[-1])
    test_false = int(lines[5].strip().split(' ')[-1])
    return number, starting_items, operation, test, test_true, test_false


def parse_input(text: str) -> dict[int, Monkey]:
    lines = text.split('\n\n')

    monkeys = {}

    for line in lines:
        monkey = Monkey(*parse_monkey_text(line))
        monkeys[monkey.number] = monkey

    return monkeys


def solve_part1(input_: str) -> int:
    monkeys = parse_input(input_)

    for _ in range(20):
        for _, monkey in monkeys.items():
            while monkey.has_items():
                pass_to, item = monkey.inspect_item()
                monkeys[pass_to].catch_item(item)

    items_inspected = sorted([monkey.items_inspected for monkey in monkeys.values()], reverse=True)

    return items_inspected[0] * items_inspected[1]


def solve_part2(input_: str) -> int:
    monkeys = parse_input(input_)
    lcm_mod = lcm(*[m.divisible_by for m in monkeys.values()])

    for i in range(10000):
        for _, monkey in monkeys.items():
            while monkey.has_items():
                pass_to, item = monkey.inspect_item(relief=False, mod=lcm_mod)
                monkeys[pass_to].catch_item(item)

    items_inspected = sorted([monkey.items_inspected for monkey in monkeys.values()], reverse=True)

    return items_inspected[0] * items_inspected[1]


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
