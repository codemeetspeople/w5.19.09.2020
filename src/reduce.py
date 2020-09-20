from typing import List, Callable
from functools import reduce

IntList = List[int]
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def my_sum(x: int, y: int) -> int:
    return x + y


def multiply(x: int, y: int) -> int:
    return x * y


def wrapper(func: Callable, sequence: IntList) -> int:
    result = sequence[0]

    for elem in sequence[1:]:
        result = func(result, elem)

    return result


print(wrapper(my_sum, array))
print(wrapper(multiply, array))
print()

print(wrapper(lambda x, y: x + y, array))
print(wrapper(lambda x, y: x * y, array))
print()

print(reduce(lambda x, y: x + y, array))
print(reduce(lambda x, y: x * y, array))
