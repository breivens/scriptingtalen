def expression(nums: list or tuple, operators: str or list or tuple) -> str:
    assert (all(isinstance(n, int) and n > 0 for n in nums)
            and len(nums) == len(operators) + 1
            and set(operators) <= {'+', '-', '|'}), 'invalid expression'
    return f"{' '.join([f'{x} {y}' for x, y in zip(nums, operators)])} {nums[-1]}".replace(' | ', '')


def result(nums: list or tuple, operators: str or list or tuple) -> int:
    return eval(expression(nums, operators))


def plusminus(target: int, numbers=tuple(range(1, 10))) -> set:
    assert all(isinstance(n, int) and n > 0 for n in numbers), 'invalid numbers'
    from itertools import chain

    def _plusminus(remaining: int, nums: list, operations: str) -> list:
        if len(nums) == 1:
            return [expression(numbers, operations)] if remaining - nums[0] == 0 else []

        return list(chain(_plusminus(remaining - nums[0], nums[1:], operations + '+'),
                          _plusminus(remaining - nums[0], [-nums[1]] + nums[2:], operations + '-'),
                          _plusminus(remaining, [int(str(nums[0]) + str(nums[1]))] + nums[2:], operations + '|')))

    return set(_plusminus(remaining=target, nums=list(numbers), operations=''))


def result_no_eval(nums: list or tuple, operators: str or list or tuple) -> int:
    expr = expression(nums, operators).split()
    while len(expr) != 1:
        (x, o, y), expr = expr[:3], expr[3:]
        num = {'+': int(x) + int(y), '-': int(x) - int(y)}[o]
        expr.insert(0, str(num))
    return expr[0]
