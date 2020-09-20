import pytest

from generators import my_range


@pytest.mark.parametrize('range_args, sequence', [
    ((3,), (0, 1, 2)),
    ((3, 0, -1), (3, 2, 1)),
    ((1, 3), (1, 2))
])
def test_range(range_args, sequence):
    generator = my_range(*range_args)

    for value in sequence:
        assert next(generator) == value

    with pytest.raises(StopIteration):
        next(generator)


@pytest.mark.parametrize('exception_type, parameters', [
    (TypeError, ()),
    (TypeError, (1, 2, 3, 4)),
    (TypeError, (1, 'wrong', 1)),
    (TypeError, ('wrong', 2, 1)),
    (TypeError, (1, 3, 'wrong')),
    (ValueError, (1, 5, 0)),
    (ValueError, (1, -5, 1)),
    (ValueError, (-1, 5, 1)),
    (ValueError, (1, 5, -1))
])
def test_range_exception(exception_type, parameters):
    with pytest.raises(exception_type):
        gen = my_range(*parameters)
        next(gen)
