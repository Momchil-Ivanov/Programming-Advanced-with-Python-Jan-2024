from math import floor
from core import execute_expression

expression = input()


def truncate(f, n):
    return floor(f * 10 ** n) / 10 ** n


result = execute_expression(expression)
print(f'{truncate(result, 2)}')