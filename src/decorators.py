def run_n_times(times):
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                func(*args, **kwargs)

        wrapper.__name__ = func.__name__
        return wrapper
    return outer_wrapper


@run_n_times(5)
def hello(username='caiman'):
    print(f'Hello, {username}!')


@run_n_times(3)
def multiply(x, y):
    print(f'{x * y}')


multiply(3, 8)
hello(username='user1')
