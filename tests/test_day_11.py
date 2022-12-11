import pytest

from aoc2022 import day_11 as day


@pytest.fixture
def mock_input():
    return """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


def test_parse_monkey_text():
    input_ = """Monkey 3:
Starting items: 74
Operation: new = old + 3
Test: divisible by 17
If true: throw to monkey 0
If false: throw to monkey 1"""
    expected = (3, ('74',), ('+', 3), 17, 0, 1)
    result = day.parse_monkey_text(input_)
    assert (x == result[i] for i, x in enumerate(expected))


def test_solve_part1(mock_input):
    expected = 10605
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 2713310158
    result = day.solve_part2(mock_input)
    assert expected == result
