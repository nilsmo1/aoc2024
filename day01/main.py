# Day 1

# Question 1
def question1(puzzle):
    total = 0
    left, right = puzzle
    left.sort()
    right.sort()
    for l, r in zip(left, right):
        total += abs(r - l)
    return total

# Question 2
def question2(puzzle):
    total = 0
    left, right = puzzle
    left.sort()
    for l in left:
        total += l * right.count(l)
    return total

# Input
def parse_input(file):
    with open(file, 'r') as inp:
        left, right = [], []
        for line in inp.read().splitlines():
            l, r = [int(i) for i in line.split('   ')]
            left.append(l)
            right.append(r)
        return (left, right)

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')

    # Tests
    t1, ans1 = question1(sample_input), 11
    t2, ans2 = question2(sample_input), 31
    assert t1 == ans1, t1
    assert t2 == ans2, t2

    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    print(f'Q1: {question1(puzzle_input)}')
    print(f'Q2: {question2(puzzle_input)}')
