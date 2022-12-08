import pytest

from aoc2022 import day_07 as day


@pytest.fixture
def mock_input():
    return """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


def test_solve_part1(mock_input):
    expected = 95437
    result = day.solve_part1(mock_input)
    assert expected == result


def test_root_size(mock_input):
    expected = 48381165
    commands = mock_input.strip().split('\n')
    directory_dict = day.walk_directory(commands)

    result = directory_dict[('/',)].get_size()

    assert result == expected


def test_solve_part2(mock_input):
    expected = 24933642
    result = day.solve_part2(mock_input)
    assert expected == result
