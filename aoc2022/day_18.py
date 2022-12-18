from pathlib import Path
from typing import NamedTuple

from aoc2022 import AOC_DIR
from aoc2022.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202218_input.txt'


class Cube(NamedTuple):
    x: int
    y: int
    z: int


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_input(text: str) -> list[Cube]:
    lines = text.strip().split('\n')
    cubes = [(int(x) for x in cube.split(',')) for cube in lines]
    return [Cube(*cube) for cube in cubes]


def are_connected(c1, c2) -> int:
    if (c1.x == c2.x) and (c1.y == c2.y):
        if abs(c1.z - c2.z) == 1:
            return 1
    elif (c1.y == c2.y) and (c1.z == c2.z):
        if abs(c1.x - c2.x) == 1:
            return 1
    elif (c1.x == c2.x) and (c1.z == c2.z):
        if abs(c1.y - c2.y) == 1:
            return 1
    return 0


def get_neighbors(cube: Cube) -> list[Cube]:
    x, y, z = cube.x, cube.y, cube.z
    return [
        Cube(x - 1, y, z),
        Cube(x + 1, y, z),
        Cube(x, y - 1, z),
        Cube(x, y + 1, z),
        Cube(x, y, z - 1),
        Cube(x, y, z + 1),
    ]


def find_stream(box: list[Cube], cubes: list[Cube]) -> set[Cube]:
    visited = set()
    unvisited = {Cube(-1, -1, -1)}
    while unvisited:
        check = unvisited.pop()
        if check in cubes:
            continue
        else:
            visited.update([check])
            unvisited.update([n for n in get_neighbors(check) if (n not in visited) and (n in box)])
    return visited


def solve_part1(input_: str) -> int:
    cubes = parse_input(input_)

    connected = 0
    for i, cube1 in enumerate(cubes[:-1]):
        for cube2 in cubes[i:]:
            connected += are_connected(cube1, cube2)

    return 6 * len(cubes) - 2 * connected


def solve_part2(input_: str) -> int:
    cubes = parse_input(input_)
    x_min, *_, x_max = sorted([cube.x for cube in cubes])
    y_min, *_, y_max = sorted([cube.y for cube in cubes])
    z_min, *_, z_max = sorted([cube.z for cube in cubes])

    bounding_box = []
    for x in range(-1, x_max + 2):
        for y in range(-1, y_max + 2):
            for z in range(-1, z_max + 2):
                if (cube := Cube(x, y, z)) not in cubes:
                    bounding_box.append(cube)

    stream = find_stream(bounding_box, cubes)

    surface_area = 0
    for outside_cube in stream:
        for cube in cubes:
            surface_area += are_connected(outside_cube, cube)

    return surface_area


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
