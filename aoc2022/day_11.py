from math import floor
from pathlib import Path
from  collections import deque

from aoc2022 import AOC_DIR
from aoc2022.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202211_input.txt'


class Monkey:
    def __init__(self, number: int, items: tuple[int], operation: tuple[str],
                 test: int, test_true: int, test_false: int):
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

    def _initialize_items(self, items: tuple[int]):
        item_list = deque([])
        for item in items:
            item_list.append(item)
        return item_list

    def print_items(self) -> str:
        return ', '.join([str(x) for x in self.holding_items])

    def has_items(self) -> bool:
        if len(self.holding_items):
            return True
        return False

    def inspect_item(self, relief: bool = True) -> tuple[int, int]:

        self.items_inspected += 1

        item = self.holding_items.popleft()

        if self.operation == ('*', 'old'):
            item = item * item
        elif self.operation[0] == '+':
            item = item + int(self.operation[1])
        elif self.operation[0] == '*':
            item = item * int(self.operation[1])
        else:
            raise ValueError(f'operation {self.operation} has unexpected value')

        if relief:
            item = floor(item / 3)

        if (item % self.divisible_by) == 0:
            return self.pass_if_true, item
        else:
            return self.pass_if_false, item

    def catch_item(self, item):
        self.holding_items.append(item)

    def catch_items(self, items: list[int]):
        self.holding_items.extend(items)

    def square_worry(self, worry: int):
        return worry * worry

    def add_worry(self, worry: int):
        return worry + int(self.operation[1])

    def multiply_worry(self, worry: int):
        return worry * int(self.operation[1])

    def pick_operation(self):
        if self.operation == ('*', 'old'):
            return self.square_worry
        elif self.operation[0] == '+':
            return self.add_worry
        elif self.operation[0] == '*':
            return self.multiply_worry
        else:
            raise ValueError(f'{self.operation} did not match')

    def batch_inspect(self):
        self.items_inspected = len(self.holding_items)

        self.holding_items = [self.operation_func(x) for x in self.holding_items]


class Item:
    def __init__(self, worry):
        self.ops = [worry]

    def add_worry(self, num):
        self.ops = [stored + num for stored in self.ops]

    def multiply_worry(self, num):
        self.ops.append(num)

    def square_worry(self):
        self.ops = 2 * self.ops

    def is_divisible(self, num):
        return any((worry % num) == 0 for worry in self.ops)

    def __str__(self):
        return f"[{', '.join(str(x) for x in self.ops)}]"

    def __repr__(self):
        return f"Item({self.__str__()})"


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_items(text: str):
    idx = text.find(':')
    return text[idx + 2:].split(', ')


def parse_monkey_text(text: str):
    # breakpoint()
    text = text.strip().split('\n')
    number = int(text[0][-2])
    starting_items = tuple(int(x) for x in parse_items(text[1]))
    operation = tuple(text[2].strip().split(' ')[-2:])
    test = int(text[3].strip().split(' ')[-1])
    test_true = int(text[4].strip().split(' ')[-1])
    test_false = int(text[5].strip().split(' ')[-1])
    return number, starting_items, operation, test, test_true, test_false


def parse_input(text: str):
    text = text.split('\n\n')

    monkeys = {}

    for monkey in text:
        monkey = parse_monkey_text(monkey)
        monkeys[monkey[0]] = Monkey(*monkey)

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


def solve_part2(input_: str):
    monkeys = parse_input(input_)

    for i in range(10000):
        if (i % 20) == 0:
            for m in monkeys.values():
                print(m, end=' ')
            print(i)
        for _, monkey in monkeys.items():
            while monkey.has_items():
                pass_to, item = monkey.inspect_item(relief=False)
                monkeys[pass_to].catch_item(item)

    items_inspected = sorted([monkey.items_inspected for monkey in monkeys.values()], reverse=True)

    return items_inspected[0] * items_inspected[1]


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    # result2 = solve_part2(input_)
    result2 = None

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
