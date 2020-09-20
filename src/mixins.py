class Numeric:
    def _validate(self, value):
        return value

    def __init__(self, value=0):
        self._value = self._validate(value)

    def __str__(self):
        return f'{self.value}'

    @property
    def value(self):
        return self._value


class Integer(Numeric):
    def _validate(self, value):
        return int(value)


class Float(Numeric):
    def _validate(self, value):
        return float(value)


class SquareMixin:
    def square(self):
        return self.value ** 2


class AbsoluteMixin:
    def absolute(self):
        return self.value * -1 if self.value < 0 else self.value


class IntegerSquared(Integer, SquareMixin):
    pass


class IntegerAbsolute(Integer, AbsoluteMixin):
    pass


integer = IntegerSquared(10)
