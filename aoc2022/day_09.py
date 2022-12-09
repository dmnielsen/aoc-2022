from pathlib import Path

from aoc2022 import AOC_DIR
from aoc2022.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202209_input.txt'


Loc = tuple[int, int]


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_input(text: str):
    lines = text.strip().split('\n')
    steps = []
    for line in lines:
        dir, num = line.split(' ')
        steps.append((dir, int(num)))
    return steps


def is_touching(h: Loc, t: Loc) -> bool:
    x_diff = abs(h[0] - t[0])
    y_diff = abs(h[1] - t[1])
    if (0 <= x_diff <= 1) and (0 <= y_diff <= 1):
        return True
    return False


def move_head(dir, curr_loc) -> Loc:
    x, y = curr_loc
    if dir == 'R':
        return x + 1, y
    elif dir == 'L':
        return x - 1, y
    elif dir == 'U':
        return x, y + 1
    else:
        return x, y - 1


def move_tail(tail_loc: Loc, head_loc: Loc) -> Loc:
    tx, ty = tail_loc
    hx, hy = head_loc
    diff_x = hx - tx
    diff_y = hy - ty
    if diff_x == 2:
        diff_x = 1
    elif diff_x == -2:
        diff_x = -1
    elif diff_y == 2:
        diff_y = 1
    elif diff_y == -2:
        diff_y = -1
    return tx + diff_x, ty + diff_y


def move_tail_part2(tail_loc: Loc, head_loc: Loc) -> Loc:
    tx, ty = tail_loc
    hx, hy = head_loc
    diff_x = hx - tx
    diff_y = hy - ty
    if diff_x == 2:
        diff_x = 1
    elif diff_x == -2:
        diff_x = -1
    if diff_y == 2:
        diff_y = 1
    elif diff_y == -2:
        diff_y = -1
    return tx + diff_x, ty + diff_y


def simulate_movements(move_list: list[Loc]) -> set[Loc]:
    H = (0, 0)
    T = (0, 0)
    locs = {(0, 0)}

    for dir, n_steps in move_list:
        for i in range(n_steps):
            # move head
            H = move_head(dir, H)
            # check if touching
            if not is_touching(H, T):
                # if yes, move tail
                T = move_tail(T, H)
                locs.update([T])
    return locs


def initialize_knots() -> dict[int, Loc]:
    return {i: (0, 0) for i in range(10)}


def simulate_ten_knots(move_list: list[Loc]) -> set[Loc]:
    tail_locs = {(0, 0)}
    knots = initialize_knots()

    for dir, n_steps in move_list:
        for _ in range(n_steps):
            knots[0] = move_head(dir, knots[0])

            # check each subsequent knot
            for j in range(1, 10):
                if not is_touching(knots[j - 1], knots[j]):
                    knots[j] = move_tail_part2(knots[j], knots[j - 1])

                    if j == 9:
                        tail_locs.update([knots[9]])

    return tail_locs


def solve_part1(input_: str) -> int:
    moves = parse_input(input_)
    tail_positions = simulate_movements(moves)
    return len(tail_positions)


def solve_part2(input_: str) -> int:
    moves = parse_input(input_)
    tail_positions = simulate_ten_knots(moves)
    return len(tail_positions)


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
