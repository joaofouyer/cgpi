# coding: utf-8
from gui.animation import Animation
from gui.window import Window
from primitives.coordinate import Coordinate
from primitives.point_graph import PointGraph


def test_animation():
    w = Window(title="Testando animação", width=500, height=500, background="#ffffff")
    a = Animation(window=w, speed=45)
    x = 250
    for y in range(100, 400):
        c = Coordinate(x=x, y=y)
        p = PointGraph(window=w, coordinate=c)
        a.append_frame(frame=p)
    assert len(a.frame) == 300
