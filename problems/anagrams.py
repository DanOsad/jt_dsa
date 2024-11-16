from checker import Checker

def is_anagram(s1: str, s2: str) -> bool:
    return counter(s1) == counter(s2)

def counter(s: str) -> dict:
    count = {}
    for c in s:
        if c not in count:
            count[c] = 0
        count[c] += 1
    return count

test_cases = [
    {
        'input': ('cats', 'tocs'),
        'solution': False
    },
    {
        'input': ('restful', 'fluster'),
        'solution': True
    },
    {
        'input': ('abbcd', 'cddba'),
        'solution': False
    },
    {
        'input': ('cats', 'tacs'),
        'solution': True
    },
]

Checker(func=is_anagram, tests=test_cases).run_tests()