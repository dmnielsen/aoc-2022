from collections import deque

import pytest

from aoc2022 import day_05 as day


@pytest.fixture
def mock_input():
    return """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def test_parse_instructions(mock_input):
    expected = [(1, 1, 0), (3, 0, 2), (2, 1, 0), (1, 0, 1)]
    result = day.parse_instructions(mock_input.split('\n\n')[1])
    assert all(instruction == result[i] for i, instruction in enumerate(expected))


def test_parse_stack_return_deque(mock_input):
    expected = [
        deque(['Z', 'N']),
        deque(['M', 'C', 'D']),
        deque(['P']),
    ]
    result = day.parse_stack(mock_input.split('\n\n')[0])
    print(result)
    assert all([crate == result[i][j] for i, stack in enumerate(expected) for j, crate in enumerate(stack)])


def test_parse_stack_returns_list_if_return_stack_is_false(mock_input):
    expected = [
        deque(['Z', 'N']),
        deque(['M', 'C', 'D']),
        deque(['P']),
    ]
    result = day.parse_stack(mock_input.split('\n\n')[0], return_stack=False)
    assert all([crate == result[i][j] for i, stack in enumerate(expected) for j, crate in enumerate(stack)])


def test_solve_part1(mock_input):
    expected = 'CMZ'
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 'MCD'
    result = day.solve_part2(mock_input)
    assert expected == result
