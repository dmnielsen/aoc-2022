from typing import Any, Tuple, Union


def _format_alt_text(alt_text: Union[str, Tuple[str, str]]) -> Tuple[str, str]:
    if alt_text:
        if isinstance(alt_text, str):
            alt_text += ':\t'
            alt_text = (alt_text, alt_text)
        elif isinstance(alt_text, tuple):
            alt_text = tuple(x + ':\t' for x in alt_text)
    else:
        alt_text = ('', '')
    return alt_text


def print_solutions(
    part1: Any = '', part2: Any = '', alt_text: Union[str, Tuple[str, str]] = ''
) -> None:
    alt_text = _format_alt_text(alt_text)
    output_str = f"""
********************************

------
Part 1
------
{alt_text[0]}{part1}

------
Part 2
------
{alt_text[1]}{part2}

********************************
"""
    print(output_str)
