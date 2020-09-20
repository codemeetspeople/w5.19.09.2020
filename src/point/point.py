from typing import Any
from math import hypot


class Point:
    __slots__ = ['_x', '_y']

    @staticmethod
    def _validate(value: float) -> float:
        try:
            return float(value)
        except (TypeError, ValueError):
            raise TypeError('Point coords should be numeric')

    def __init__(self, x=0, y=0):
        self._x = self._validate(x)
        self._y = self._validate(y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: Any) -> bool:
        return not self == other

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value):
        self._x = self._validate(value)

    @y.setter
    def y(self, value):
        self._y = self._validate(value)

    def distance(self, other: Any) -> float:
        if not isinstance(other, self.__class__):
            raise TypeError('Argument should be Point type')
        return hypot(self.x - other.x, self.y - other.y)
