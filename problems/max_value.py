from checker import Checker

def max_value(num_arr: list) -> int:
    max_val = float('-inf')
    for num in num_arr:
        if num > max_val:
            max_val = num
    return max_val

test_cases = [
    {
        'input': [1,7,3,5,9,2],
        'solution': 9
    },
    {
        'input': [-7,-1,-3],
        'solution': -1
    },
    {
        'input': [-2,-9,1029,5,7],
        'solution': 1029
    },
]

Checker(func=max_value, tests=test_cases).run_tests()