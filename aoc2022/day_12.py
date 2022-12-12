import string
from collections import namedtuple
from copy import deepcopy
from pathlib import Path
from typing import Optional, Union

from aoc2022 import AOC_DIR
from aoc2022.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202212_input.txt'


Coords = namedtuple('Coords', ['x', 'y'])

LETTER_VAL = {s: val for val, s in enumerate(string.ascii_lowercase)}


class Node:
    def __init__(self, coords: Coords, height: int, neighbors: list[Coords]):
        self.coords = coords
        self.height = int(height)
        self.neighbors = neighbors

        self._cost: Union[int, float] = float('inf')
        self._parent = None

    def __repr__(self):
        return f"Node(coords={self.coords}, height={self.height}, neighbors={self.neighbors})"

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    def validate_neighbors(self, grid):
        """remove any neighbors that have heights that you can't get to"""
        self.neighbors = [point for point in self.neighbors if grid[point].height <= (self.height + 1)]


# set typing for the Grid
Grid = dict[Coords, Node]


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_input(text: str) -> tuple[Grid, Coords, Coords]:
    """Returns grid, Start coordinates, End coordinates"""
    lines = text.split()
    max_rows, max_cols = len(lines), len(lines[0])

    grid_points = set((x, y) for x in range(max_cols) for y in range(max_rows))

    grid = {}

    start_point = Coords(0, 0)
    end_point = Coords(0, 0)

    for y, row in enumerate(lines):
        for x, letter in enumerate(row):

            coords = Coords(x, y)

            neighbors = [
                Coords(*point) for point in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if point in grid_points
            ]

            if letter == 'S':
                start_point = coords
                letter = 'a'
            elif letter == 'E':
                end_point = coords
                neighbors = []  # Remove neighbors, since this is the destination
                letter = 'z'

            height = LETTER_VAL[letter]

            node = Node(coords, height, neighbors)

            grid[coords] = node

    # set starting point to have zero cost and zero risk
    # grid[start_point].cost = 0

    return grid, start_point, end_point


def get_lowest_cost_node(grid: dict[Coords, int], processed: set[Coords]) -> Optional[Coords]:
    for coords, cost in sorted(grid.items(), key=lambda x: x[1]):
        if coords not in processed:
            return coords
    print('problem')
    return None


def find_path(grid: Grid, start: Coords, end: Coords) -> int:
    # set the starting point cost to zero
    grid = deepcopy(grid)
    grid[start].cost = 0

    processed: set[Coords] = set()
    unprocessed_with_cost = {start: 0}

    node_coords = get_lowest_cost_node(unprocessed_with_cost, processed)
    while node_coords is not None:
        # breakpoint()
        if node_coords == end:
            return grid[node_coords].cost

        node_info = grid[node_coords]
        for n in node_info.neighbors:
            new_cost = node_info.cost + 1
            if new_cost < grid[n].cost:
                grid[n].cost = new_cost
                grid[n].parent = node_coords
                if n not in processed:
                    unprocessed_with_cost[n] = new_cost
        processed.update([node_coords])
        node_coords = get_lowest_cost_node(unprocessed_with_cost, processed)
    return grid[end].cost


def solve_part1(input_: str) -> int:
    grid, start, end = parse_input(input_)

    # update neighbors to remove any inaccessible ones
    # breakpoint()
    for node in grid.values():
        node.validate_neighbors(grid)

    return find_path(grid, start, end)


def solve_part2(input_: str, test=False):
    grid, start, end = parse_input(input_)

    for node in grid.values():
        node.validate_neighbors(grid)

    if test:
        possible_starts = [coords for coords, node in grid.items() if (node.height == 0)]
    else:
        possible_starts = [Coords(0, i) for i in range(41)]
    print(f"Possible starting points: {len(possible_starts)}")

    path_lens = []
    for i, starting_point in enumerate(possible_starts):
        if (i % 100) == 0:
            print(i)
        path_lens.append(find_path(grid, starting_point, end))
    return min(path_lens)


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
