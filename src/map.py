array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def increment(x):
    return x + 1


def power(x):
    return x ** 2


def wrapper(func, sequence):
    result = []

    for elem in sequence:
        result.append(func(elem))

    return result


print(array)
print(wrapper(increment, array))
print(wrapper(power, array))
print()

print(array)
print(wrapper(lambda x: x + 1, array))
print(wrapper(lambda x: x ** 2, array))
print()

print(array)
print(list(map(lambda x: x + 1, array)))
print(list(map(lambda x: x ** 2, array)))
