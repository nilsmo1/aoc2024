# Day 7

from itertools import product
from math import log

# Question 1
def question1(puzzle):
    total = 0
    ops = '+*'
    for test, nums in puzzle:
        perms = product(ops, repeat=len(nums) - 1)
        for perm in perms:
            result = nums[0]
            for i, num in enumerate(nums[1:]):
                if perm[i] == '+':
                    result += num
                elif perm[i] == '*':
                    result *= num
            if result == test:
                total += test
                break
    return total

# Question 2
def question2(puzzle):
    total = 0
    ops = ['+', '*', '||']
    for test, nums in puzzle:
        perms = product(ops, repeat=len(nums) - 1)
        for perm in perms:
            result = nums[0]
            for i, num in enumerate(nums[1:]):
                if perm[i] == '+':
                    result += num
                elif perm[i] == '*':
                    result *= num
                elif perm[i] == '||':
                    result *= 10 ** (int(log(num, 10)) + 1)
                    result += num
            if result == test:
                total += test
                break
    return total

# Input
def parse_input(file):
    with open(file, 'r') as inp:
        equations = []
        for line in inp.read().splitlines():
            test, nums = line.split(': ')
            nums = [int(n) for n in nums.split()]
            equations.append((int(test), nums))
        return equations

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')

    # Tests
    t1, ans1 = question1(sample_input), 3749
    t2, ans2 = question2(sample_input), 11387
    assert t1 == ans1, f'S1: {t1} != {ans1}'
    assert t2 == ans2, f'S2: {t2} != {ans2}'

    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    print(f'Q1: {question1(puzzle_input)}')
    print(f'Q2: {question2(puzzle_input)}')
