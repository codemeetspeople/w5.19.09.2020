from functools import reduce


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def my_sum(x, y):
    return x + y


def multiply(x, y):
    return x * y


def wrapper(func, sequence):
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
