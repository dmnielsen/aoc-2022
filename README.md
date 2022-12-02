# Advent of Code 2022

Here lies my overly verbose code for solving advent of code 2022.

## Package details
(So I don't forget next year)

I have templates for each day and a script to automatically set up
skeleton scripts and download the input. 

## Getting session ID
If I haven't used the script in a while, the cookie-based `AOC_SESSION` in the `aoc2022/create_new_day.py`
script will need to be updated. To do this, open the [advent of code webpage](https://adventofcode.com/),
login via GitHub (if not logged in already), right-click and select "Inspect", select the "Network" tab,
reload the page, click on "Input", look for the "cookie" session ID, copy the ID into the `create_new_day.py` script.
