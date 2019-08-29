# coding: utf-8

from primitives.line_graph import LineGraph
from gui.window import Window
from primitives.coordinate import Coordinate
from primitives.point import Point


def test_line_y_axis():
    w = Window(title="Testando Linhas", width=1000, height=1000, background="#000000")
    coordinate_p1 = Coordinate(x=50, y=5)
    p1 = Point(window=w, coordinate=coordinate_p1)
    coordinate_p2 = Coordinate(x=50, y=990)
    p2 = Point(window=w, coordinate=coordinate_p2)
    line = LineGraph(p1=p1, p2=p2, color="#ffffff", thickness=2)
    line.draw(w=w, animation=False)
    w.root.update()
