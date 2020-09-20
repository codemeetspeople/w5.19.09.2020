import pytest

from point.point import Point


def test_point_constructor():
    point = Point()
    assert point.x == 0.0
    assert point.y == 0.0

    point = Point(1, 3)
    assert point.x == 1.0
    assert point.y == 3.0


def test_point_properties():
    point = Point()

    assert point.x == 0.0
    assert point.y == 0.0

    point.x = 10.0
    point.y = 10.0

    assert point.x == 10.0
    assert point.y == 10.0


def test_point_operators():
    a = Point()
    b = Point()
    c = Point(2, 10)

    assert a == b
    assert not a != b
    assert b != c
    assert not b == c


def test_point_exception():
    with pytest.raises(TypeError):
        Point('wrong', 'value')


def test_point_representation():
    point = Point()

    repr_string = repr(point)
    point_string = str(point)

    assert repr_string == '(0.0, 0.0)'
    assert point_string == '(0.0, 0.0)'


def test_point_distance():
    a = Point()
    b = Point(10, 10)

    distance = a.distance(b)

    assert distance == 14.142135623730951
