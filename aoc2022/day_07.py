from pathlib import Path
from typing import Union

from aoc2022 import AOC_DIR
from aoc2022.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202207_input.txt'


class Directory:
    def __init__(self, name: tuple):
        self.name = name
        self.children = []

    def get_size(self) -> int:
        size = 0
        for child in self.children:
            if isinstance(child, File):
                size += child.size
            else:
                size += child.get_size()
        return size

    def add_child(self, child) -> None:
        self.children.append(child)


class File:
    def __init__(self, name: str, size: Union[int, str]):
        self.name = name
        self.size = None
        self.format_size(size)

    def format_size(self, size):
        self.size = int(size)

    def __repr__(self):
        return f"File(name='{self.name}', size={self.size})"


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def walk_directory(cmds: list[str]) -> dict:
    root = Directory(name=('/',))
    directory_dict: dict[tuple, File] = {('/',): root}
    current_dir = tuple()
    current_dir_obj = None
    # breakpoint()
    for i, cmd in enumerate(cmds):
        if cmd == '$ ls':
            continue
        elif cmd == '$ cd ..':
            current_dir = current_dir[:-1]
        elif cmd.startswith('$ cd '):
            current_dir += (cmd.split(' ')[-1],)
            current_dir_obj = directory_dict[current_dir]
        elif cmd.startswith('dir '):
            dirname = cmd.split(' ')[-1]
            dir_obj = Directory(name=current_dir + (dirname,))

            # add to current dir obj
            current_dir_obj.add_child(dir_obj)

            # Add new obj to dict
            directory_dict[dir_obj.name] = dir_obj
        else:
            size, name = cmd.split(' ')
            obj = File(name=current_dir + (name,), size=size)
            current_dir_obj.add_child(obj)
    return directory_dict


def get_directory_sizes(directories: dict):
    sizes = []
    for name, obj in directories.items():
        sizes.append(obj.get_size())
    return sizes


def solve_part1(input_: str):
    commands = input_.strip().split('\n')
    directory_dict = walk_directory(commands)

    sizes = get_directory_sizes(directory_dict)

    return sum(size for size in sizes if size <= 100000)


def solve_part2(input_: str):
    total_disk_space = 70000000
    needed_for_update = 30000000

    commands = input_.strip().split('\n')
    directory_dict = walk_directory(commands)

    used_space = directory_dict[('/',)].get_size()

    minimum_to_delete = needed_for_update - (total_disk_space - used_space)

    sizes = get_directory_sizes(directory_dict)

    return min(size for size in sorted(sizes) if size >= minimum_to_delete)


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
