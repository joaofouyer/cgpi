# coding: utf-8
from primitives.coordinate import Coordinate


def test_coordinate():
    coordinate = Coordinate(x=50, y=50)
    assert type(coordinate) == Coordinate
    assert coordinate.x == 50
    assert coordinate.y == 50
    assert coordinate.get_coordinate() == (50, 50)
