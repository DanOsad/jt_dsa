
class Checker:
    def __init__(self, *args, **kwargs):
        self.solver_func = kwargs.pop('func', None)
        self.tests = kwargs.pop('tests', [])
    
    def validate(self):
        if not self.examples:
            raise ValueError('No tests provided')

    def run_tests(self):
        for i, test in enumerate(self.tests, 1):
            inputs = test.get('input')
            solution = test.get('solution')
            result = self.solver_func(inputs)
            passed = result == solution
            print(f'Test {i}) Expected {solution} | Got {result} -> {self.pass_fail(passed)}')

    def pass_fail(self, result: bool):
        return 'FAILED' if not result else 'PASSED'