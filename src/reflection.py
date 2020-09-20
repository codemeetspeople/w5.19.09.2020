class Integer:
    def __init__(self, value=0):
        self.value = int(value)

    def __str__(self):
        return f'{self.value}'

    def __repr__(self):
        return f'{self.value}'

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Integer(self.value + other.value)
        return NotImplemented


class Float:
    def __init__(self, value=0.0):
        self.value = float(value)

    def __str__(self):
        return f'{self.value}'

    def __repr__(self):
        return f'{self.value}'

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Float(self.value + other.value)
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Integer):
            return Integer(int(self.value) + other.value)
        return NotImplemented
