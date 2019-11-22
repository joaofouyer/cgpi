from primitives.point import Point


def test_point():
    p1 = Point(x=300, y=300)

    assert type(p1) == Point
    assert p1.get_coordinates() == (p1.x, p1.y)

    p2 = p1.find_p2(length=100, angle=0)
    assert p2.x == 400
    assert p2.y == 300
    assert p2.get_coordinates() == (400, 300)
