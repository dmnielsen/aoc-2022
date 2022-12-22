import pytest

from aoc2022 import day_21 as day


@pytest.fixture
def mock_input():
    return """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32"""


def test_solve_part1(mock_input):
    expected = 152
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 301
    result = day.solve_part2(mock_input)
    assert expected == result
