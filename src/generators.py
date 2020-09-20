def my_range(*args):
    args_count = len(args)

    if args_count < 1 or args_count > 3:
        raise TypeError(
            f'my_range expected at most 3 arguments, got {args_count}'
        )

    try:
        if len(args) == 1:
            start, finish, step = 0, int(args[0]), 1
        elif len(args) == 2:
            start, finish, step = int(args[0]), int(args[1]), 1
        else:
            start, finish, step = int(args[0]), int(args[1]), int(args[2])
    except (ValueError, TypeError):
        raise TypeError('my_range support only integer arguments type')

    if step == 0:
        raise ValueError('Invalid parameters')

    if start < 0 or finish < 0:
        raise ValueError('Invalid parameters')

    if step < 0:
        if start < finish:
            raise ValueError('Invalid parameters')

    if step > 0:
        while start < finish:
            yield start
            start += step
    else:
        while start > finish:
            yield start
            start += step


if __name__ == '__main__':  # pragma: no cover
    print('---- my_range(5) -----')
    for i in my_range(5):
        print(i)
    print()

    print('---- my_range(5, 10) -----')
    for i in my_range(5, 10):
        print(i)
    print()

    print('---- my_range(1, 10, 2) -----')
    for i in my_range(1, 10, 2):
        print(i)
    print()

    print('---- my_range(10, 0, -2) -----')
    for i in my_range(10, 0, -2):
        print(i)
    print()
