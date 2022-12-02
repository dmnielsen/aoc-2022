import argparse as arg
import os
import sys
from pathlib import Path
from string import Template

import requests

from aoc2022.util import NEW_DAY_TEMPLATE, NEW_TEST_TEMPLATE

YEAR = 2022
AOC_BASE_URL = 'https://adventofcode.com'
FILE_DIR = Path(__file__).parent.absolute()
# USER_SESSION_ID is found by inspecting session cookie content while logged into AOC
# USER_SESSION_ID = os.environ['AOC_SESSION']
USER_SESSION_ID = '53616c7465645f5f7efa3c05cc77837defad649e5c6bfceebc2bfff48e212b43d7a14ad9eef7177bdf2814636af660b29d73ecf1e6b52820d792d58ec4a6b224'
USER_AGENT = "adventofcode_working_directories_creator"


def download_input(day: int) -> Path:
    output_filename = FILE_DIR.parent / 'inputs' / format_input_filename(day)
    url = f'{AOC_BASE_URL}/{YEAR}/day/{day}/input'

    with requests.get(
        url=url, cookies={"session": USER_SESSION_ID}, headers={"User-Agent": USER_AGENT}
    ) as response:
        if response.ok:
            data = response.text
        else:
            print('!!!!!! Server response for input is not valid !!!!!!')
            print('Exiting')
            sys.exit()

    with open(output_filename, 'w') as f:
        f.write(data)

    return output_filename


def create_day_template(day: str):
    day_filename = format_day_filename(day)
    if not validate_filename(day_filename):
        day_template = load_day_template()
        filled = day_template.safe_substitute(input_filename=format_input_filename(day))

        print(f'Writing day {day} template')
        write_file(day_filename, filled)


def create_test_template(day: str):
    test_filename = format_test_filename(day)
    if not validate_filename(test_filename):
        test_template = load_test_template()
        filled_test = test_template.safe_substitute(module_name=f'day_{day:02}')

        print(f'Writing test day_{day} template')
        write_file(format_test_filename(day), filled_test)


def load_day_template() -> Template:
    with open(NEW_DAY_TEMPLATE, 'r') as f:
        return Template(f.read())


def load_test_template() -> Template:
    with open(NEW_TEST_TEMPLATE, 'r') as f:
        return Template(f.read())


def format_day_filename(day: str) -> Path:
    return FILE_DIR / f'day_{day:02}.py'


def format_test_filename(day: str) -> Path:
    return FILE_DIR.parent / 'tests' / f'test_day_{day:02}.py'


def validate_filename(filename: Path) -> bool:
    if filename.exists():
        print(f'"{filename.name}" already exists')
        sys.exit()
    return False


def format_input_filename(day: int) -> str:
    return f'{YEAR}{day:02}_input.txt'


def write_file(filename, template):
    with open(filename, 'w') as f:
        f.write(template)


def main(args):

    if not args.input_only:
        create_day_template(args.day)

        create_test_template(args.day)

    print(f'...downloading inputs')
    downloaded = download_input(args.day)
    if downloaded.exists():
        print(f'Successfully downloaded {downloaded}')


if __name__ == '__main__':
    parser = arg.ArgumentParser(description='Build script for advent of code day')
    parser.add_argument('day', type=int)
    parser.add_argument('--input-only', action='store_true', required=False)
    args = parser.parse_args()
    main(args)
