import pytest

from aoc2022 import day_03 as day


@pytest.fixture
def mock_input():
    return """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


def test_find_badge_item():
    elf1 = 'vJrwpWtwJgWrhcsFMMfFFhFp'
    elf2 = 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'
    elf3 = 'PmmdzqPrVvPwwTWBwg'

    expected = 'r'
    result = day.find_badge_item(elf1, elf2, elf3)
    assert expected == result


def test_solve_part1(mock_input):
    expected = 157
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 70
    result = day.solve_part2(mock_input)
    assert expected == result
