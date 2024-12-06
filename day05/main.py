# Day 5

from collections import defaultdict
from functools import cmp_to_key

# Question 1
def populate_rules(rules):
    rule_dict = defaultdict(list)
    for _from, _to in rules:
        rule_dict[_from].append(_to)
    return rule_dict

def validate_page(page, rule_dict):
    for c, start in enumerate(page):
        for _, look_ahead in enumerate(page[c + 1:]):
            if start in rule_dict[look_ahead]:
                return False
    return True

def question1(puzzle):
    total = 0
    rules, pages = puzzle
    rule_dict = populate_rules(rules)

    for page in pages:
        total += page[len(page) // 2] if validate_page(page, rule_dict) else 0
    return total

# Question 2

def question2(puzzle):
    total = 0
    rules, pages = puzzle
    rule_dict = populate_rules(rules)

    def correct_page_ordering(a, b):
        if a in rule_dict[b]:
            return 1
        if b in rule_dict[a]:
            return -1
        return 0

    incorrect_pages = [page for page in pages if not validate_page(page, rule_dict)]
    for page in incorrect_pages:
        page.sort(key=cmp_to_key(correct_page_ordering))
        total += page[len(page) // 2] if validate_page(page, rule_dict) else 0
    return total

# Input
def parse_input(file):
    with open(file, 'r') as inp:
        rules, pages = inp.read().split('\n\n')
        rules = [[int(p) for p in rule.split('|')] for rule in rules.splitlines()]
        pages = [[int(p) for p in page.split(',')] for page in pages.splitlines()]
        return rules, pages

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')

    # Tests
    t1, ans1 = question1(sample_input), 143
    t2, ans2 = question2(sample_input), 123
    assert t1 == ans1, f'S1: {t1} != {ans1}'
    assert t2 == ans2, f'S2: {t2} != {ans2}'

    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    print(f'Q1: {question1(puzzle_input)}')
    print(f'Q2: {question2(puzzle_input)}')
