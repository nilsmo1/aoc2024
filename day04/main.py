# Day 4

# Question 1

def question1(puzzle):
    total = 0

    def find(row, col):
        matches = 0
        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        for r_off, c_off in directions:
            if 0 <= row + r_off * 3 < len(puzzle) and 0 <= col + c_off * 3 < len(puzzle[row]):
                if ''.join([puzzle[row + r_off * i][col + c_off * i] for i in range(4)]) == 'XMAS':
                    matches += 1
        return matches

    for r, row in enumerate(puzzle):
        for c, col in enumerate(row):
            if col == 'X':
                total += find(r, c)

    return total

# Question 2
def question2(puzzle):
    total = 0

    def find(row, col):
        matches = 0
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        if ''.join([puzzle[row + r][col + c] for r, c in directions]) in ['MSMS', 'SSMM', 'MMSS', 'SMSM']:
            matches += 1
        return matches

    for r, row in enumerate(puzzle):
        for c, col in enumerate(row):
            if r == 0 or r == len(puzzle) - 1 or c == 0 or c == len(row) -1:
                continue
            if col == 'A':
                total += find(r, c)
    return total

# Input
def parse_input(file):
    with open(file, 'r') as inp:
        return inp.read().splitlines()

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')

    # Tests
    t1, ans1 = question1(sample_input), 18
    t2, ans2 = question2(sample_input), 9
    assert t1 == ans1, f'S1: {t1} != {ans1}'
    assert t2 == ans2, f'S2: {t2} != {ans2}'

    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    print(f'Q1: {question1(puzzle_input)}')
    print(f'Q2: {question2(puzzle_input)}')
