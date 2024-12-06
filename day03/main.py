# Day 3

import re

# Question 1
def question1(puzzle):
    total = 0
    nums = [(int(x), int(y)) for _, _, x, y in puzzle if x and y]
    for x, y in nums:
        total += x * y
    return total

# Question 2
def question2(puzzle):
    total = 0
    multiply = True
    for dont, do, x, y in puzzle:
        if dont: multiply = False
        if do:   multiply = True
        if x and y and multiply:
            total += int(x) * int(y)
    return total

# Input
def parse_input(file):
    pattern = r"(don\'t\(\))|(do\(\))|mul\((\d+),(\d+)\)"
    matches = []
    with open(file, 'r') as inp:
        for line in inp.read().splitlines():
            matched = re.findall(pattern, line)
            for match in matched:
                matches.append(match)
        return matches

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample1')
    sample_input = parse_input('sample2')

    # Tests
    t1, ans1 = question1(sample_input), 161
    t2, ans2 = question2(sample_input), 48
    assert t1 == ans1, f'S1: {t1} != {ans1}'
    assert t2 == ans2, f'S2: {t2} != {ans2}'

    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    print(f'Q1: {question1(puzzle_input)}')
    print(f'Q2: {question2(puzzle_input)}')
