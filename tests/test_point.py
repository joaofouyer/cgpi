from primitives.point import Point
from primitives.coordinate import Coordinate


def test_point():
    coordinate = Coordinate(x=300, y=300)
    p1 = Point(coordinate=coordinate)

    assert type(p1) == Point
    assert type(p1.coordinate) == Coordinate
    assert p1.coordinate == coordinate
    assert p1.get_coordinates() == (p1.x, p1.y)

    p2 = p1.find_p2(length=100, angle=0)
    assert p2.x == 400
    assert p2.y == 300
    assert p2.get_coordinates() == (400, 300)
    assert p2.coordinate.x == Coordinate(x=400, y=300).x
    assert p2.coordinate.y == Coordinate(x=400, y=300).y
