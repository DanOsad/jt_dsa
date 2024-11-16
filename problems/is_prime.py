from checker import Checker
def is_prime(num: int) -> bool:
    if num < 2:
        return False
    from math import sqrt, floor
    # Naive Solution O(n) #
    # for i in [n for n in range(2, num)]:
    #     if num % i == 0:
    #         return False
    # return True
    # Optimized Solution O(sqrt(n)) #
    for i in [n for n in range(2, floor(sqrt(num)+1))]:
        if num % i == 0:
            return False
    return True


test_cases = [
    {
        'input': 7,
        'solution': True
    },
    {
        'input': 11,
        'solution': True
    },
    {
        'input': 8,
        'solution': False
    },
    {
        'input': 2017,
        'solution': True
    },
    {
        'input': 2048,
        'solution': False
    },
    {
        'input': 1,
        'solution': False
    },
]

Checker(func=is_prime, tests=test_cases).run_tests()