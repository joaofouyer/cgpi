# coding: utf-8
from primitives.line_graph import LineGraph
from gui.window import Window
from primitives.coordinate import Coordinate
from primitives.point import Point


def test_line_length_angle():
    p1 = Point(coordinate=Coordinate(x=250, y=250))
    line = LineGraph(p1=p1, length=100, angle=0)
    assert line


def test_line_slope():
    assert True


def test_line_calc_b():
    assert True


def test_line_delta_x():
    assert True


def test_line_delta_y():
    assert True


def test_line_y_axis():
    w = Window(title="Testando Iterando em Y", width=1000, height=1000, background="#000000")
    p1 = Point(coordinate=Coordinate(x=50, y=5))
    p2 = Point(coordinate=Coordinate(x=50, y=990))
    line = LineGraph(p1=p1, p2=p2, color="#ffffff", thickness=2)
    assert line.p1 == p1
    assert line.p2 == p2
    assert line.color == "#ffffff"
    assert line.thickness == 2
    assert line
    error = line.draw(w=w, animation=False)
    w.root.update()
    assert not error