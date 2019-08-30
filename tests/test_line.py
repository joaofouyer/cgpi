# coding: utf-8
from primitives.line import Line
from primitives.coordinate import Coordinate
from primitives.point import Point


def test_line_length_angle_0():
    p1 = Point(coordinate=Coordinate(x=250, y=250))
    line = Line(p1=p1, length=100, angle=0)
    assert line.p1 == p1
    assert line.p1.x == 250
    assert line.p1.y == 250
    assert line.p2.x == 350
    assert line.p2.y == 250
    assert line.m == 0
    assert line.b == 250
    assert line.calc_slope() == 0
    assert line.calc_b() == 250
    assert line.m == line.calc_slope()
    assert line.b == line.calc_b()
    assert line.delta_x_axis() == 100
    assert line.delta_y_axis() == 0
    assert line.y_linear_equation(line.p2.x) == 250
    assert line.y_linear_equation(line.p1.x) == 250


def test_line_length_angle_90():
    p1 = Point(coordinate=Coordinate(x=250, y=250))
    line = Line(p1=p1, length=100, angle=90)
    assert line.p1 == p1
    assert line.p1.x == 250
    assert line.p1.y == 250
    assert line.p2.x == 250
    assert line.p2.y == 150
    assert line.m == 0
    assert line.b == 250
    assert line.calc_slope() == 0
    assert line.calc_b() == 250
    assert line.m == line.calc_slope()
    assert line.b == line.calc_b()
    assert line.delta_x_axis() == 100
    assert line.delta_y_axis() == 0
    assert line.y_linear_equation(line.p2.x) == 250
    assert line.y_linear_equation(line.p1.x) == 250

def test_line_slope():
    assert True


def test_line_calc_b():
    assert True


def test_line_delta_x():
    assert True


def test_line_delta_y():
    assert True


def test_line_y_axis():
    p1 = Point(coordinate=Coordinate(x=50, y=5))
    p2 = Point(coordinate=Coordinate(x=50, y=990))
    line = Line(p1=p1, p2=p2)
    assert line.p1 == p1
    assert line.p2 == p2
