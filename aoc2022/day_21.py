from pathlib import Path

from aoc2022 import AOC_DIR
from aoc2022.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202221_input.txt'


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_input(text: str, replace_humn: bool = False):
    lines = text.strip().split('\n')

    monkey_numbers = {}
    monkey_operations = {}
    for line in lines:
        monkey, jobs = line.split(': ')
        job = jobs.split(' ')
        if len(job) == 1:
            monkey_numbers[monkey] = int(job[0])
            if replace_humn:
                monkey_numbers['humn'] = None

        else:
            monkey_operations[monkey] = job
    return monkey_numbers, monkey_operations


def solve_operation(num1, op, num2) -> int:
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
    else:
        # shouldn't get here
        return 0


def solve_part1(input_: str):
    nums, ops = parse_input(input_)

    root = None
    while root is None:
        # print(len(nums), len(ops))

        to_delete = []

        for monkey, operation in ops.items():
            m1 = nums.get(operation[0], None)
            m2 = nums.get(operation[-1], None)
            if m1 is not None and m2 is not None:
                nums[monkey] = int(solve_operation(m1, operation[1], m2))
                to_delete.append(monkey)
                if monkey == 'root':
                    root = nums[monkey]
                    return root
        for monkey in to_delete:
            del ops[monkey]

    return root


class Num:
    def __init__(self, name, value):
        self.name = name
        self.num = value

    def has_children(self):
        return False


class Op:
    def __init__(self, name, left, op, right, parent=None):
        self.name = name
        self.left = left
        self.right = right
        self.parent = parent
        self.op = op
        self.value = None


def reverse_operation(N, operation):
    if '*' in operation:
        operation.remove('*')
        return N / int(operation[0])
    elif '/' in operation:
        operation.remove('/')
        return N * int(operation[0])

    left, right = operation
    if left == '+':
        return N - int(right)
    elif right == '+':
        return N - int(left)
    elif left == '-':
        return N + int(right)
    elif right == '-':
        return int(left) - N


def solve_part2(input_: str):
    nums, ops = parse_input(input_, replace_humn=True)

    left, _, right = ops['root']
    del ops['root']

    size = len(ops) + 1
    while True:
        if size == len(ops):
            break
        else:
            size = len(ops)
        to_delete = []
        for monkey, operation in ops.items():
            m1 = nums.get(operation[0], None)
            m2 = nums.get(operation[-1], None)
            if m1 is not None and m2 is not None:
                nums[monkey] = int(solve_operation(m1, operation[1], m2))
                to_delete.append(monkey)

        for monkey in to_delete:
            del ops[monkey]

    for monkey, op in ops.items():
        m1 = nums.get(op[0], op[0])
        m2 = nums.get(op[-1], op[-1])
        ops[monkey] = [m1, op[1], m2]

    if nums.get(left, None) is not None:
        compare_to = nums[left]
        l, o, r = ops[right]
        if isinstance(l, int):
            monkey = r
            list_ops = [l, o]
        else:
            monkey = l
            list_ops = [o, r]
    else:
        compare_to = nums[right]
        l, o, r = ops[left]
        if isinstance(l, int):
            monkey = r
            list_ops = [l, o]
        else:
            monkey = l
            list_ops = [o, r]

    next_ops = [list_ops]
    monkey_order = [monkey]
    while True:
        ll, oo, rr = ops[monkey_order[-1]]
        if ll is None:
            next_ops.append([oo, rr])
            break
        elif rr is None:
            next_ops.append([ll, oo])
            print(ll, oo, rr)
            break
        elif isinstance(ll, str):
            monkey_order.append(ll)
            next_ops.append([oo, rr])
        elif isinstance(rr, str):
            monkey_order.append(rr)
            next_ops.append([ll, oo])
        else:
            print('problem')

    value = compare_to
    for op in next_ops:
        value = reverse_operation(value, op)

    return int(value)


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
