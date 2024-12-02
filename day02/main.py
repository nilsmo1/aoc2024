# Day 2

# Question 1
def safe(nums):
    if len(nums) < 2:
        return True
    ascending = nums[0] < nums[1]
    for a, b in zip(nums, nums[1:]):
        if ((a < b and not ascending) or
            (a > b and ascending)     or
            (not 0 < abs(a - b) < 4)  or
            (a == b)):
            return False
    return True

def question1(puzzle):
    return len([1 for line in puzzle if safe(line)])

# Question 2
def remove_one(nums):
    for i, _ in enumerate(nums):
        if safe(nums[:i] + nums[i+1:]):
            return True
    return False

def question2(puzzle):
    return len([1 for line in puzzle if remove_one(line)])

# Input
def parse_input(file):
    with open(file, 'r') as inp:
        lines = []
        for line in inp.read().splitlines():
            lines.append([int(i) for i in line.split(' ')])
        return lines

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')

    # Tests
    t1, ans1 = question1(sample_input), 2
    t2, ans2 = question2(sample_input), 4
    assert t1 == ans1, t1
    assert t2 == ans2, t2

    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    print(f'Q1: {question1(puzzle_input)}')
    print(f'Q2: {question2(puzzle_input)}')
