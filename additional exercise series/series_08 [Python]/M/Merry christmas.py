def solution(string: str, indices='0123456789') -> dict:
    assert (string.isupper() and len(set(string)) == len(string) == 10 and
            indices.isdigit() and len(set(indices)) == len(indices) == 10), 'invalid solution'
    return dict(zip(string, map(int, indices)))


def replace(string: str, solution: dict) -> str:
    assert set(string) <= set(solution) | {' '}, 'invalid puzzle'
    return ''.join([str(solution.get(char, char)) for char in string])


def issquare(number: int) -> bool:
    from math import floor, ceil, sqrt
    number = sqrt(number)
    return floor(number) == ceil(number)


def iscorrect(sentence: str, solution_string: str, *indices: str) -> bool:
    solution_dict = solution(solution_string, *indices)
    return all(issquare(int(replace(word, solution_dict))) for word in sentence.split())
