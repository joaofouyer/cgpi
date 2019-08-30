# coding: utf-8

from gui.window import Window
from primitives.coordinate import Coordinate
from primitives.point_graph import PointGraph
from primitives.point import Point
from primitives.line_graph import LineGraph
from primitives.line import Line
from primitives.circle import Circle
from primitives.circle_graph import CircleGraph



def draw():
    try:
        w = Window(title="Desenho da Sala", width=700, height=700, background="#FFFFFF")
        center = PointGraph(coordinate=Coordinate(x=350, y=350), window=w, size=2, color="#000000")
        line = LineGraph(p1=center, length=300, angle=270)
        line.draw(w=w, animation=True)
        inner_line = LineGraph(p1=center, length=150, angle=0)
        inner_line.draw(w=w, animation=True)
        circle = CircleGraph(center=inner_line.p2.coordinate, radius =150, color="#008000", thickness=2)
        circle.draw_circle(window=w)

        line = LineGraph(p1=center, length=300, angle=90)
        line.draw(w=w, animation=True)
        inner_line = LineGraph(p1=center, length=150, angle=60)
        inner_line.draw(w=w, animation=True)
        circle = CircleGraph(center=inner_line.p2.coordinate, radius =150, color="#008000", thickness=2)
        circle.draw_circle(window=w)

        line = LineGraph(p1=center, length=300, angle=30)
        line.draw(w=w, animation=True)
        inner_line = LineGraph(p1=center, length=150, angle=120)
        inner_line.draw(w=w, animation=True)
        circle = CircleGraph(center=inner_line.p2.coordinate, radius =150, color="#008000", thickness=2)
        circle.draw_circle(window=w)

        line = LineGraph(p1=center, length=300, angle=150)
        line.draw(w=w, animation=True)
        inner_line = LineGraph(p1=center, length=150, angle=180)
        inner_line.draw(w=w, animation=True)
        circle = CircleGraph(center=inner_line.p2.coordinate, radius =150, color="#008000", thickness=2)
        circle.draw_circle(window=w)

        line = LineGraph(p1=center, length=300, angle=210)
        line.draw(w=w, animation=True)
        inner_line = LineGraph(p1=center, length=150, angle=240)
        inner_line.draw(w=w, animation=True)
        circle = CircleGraph(center=inner_line.p2.coordinate, radius =150, color="#008000", thickness=2)
        circle.draw_circle(window=w)

        line = LineGraph(p1=center, length=300, angle=330)
        line.draw(w=w, animation=True)
        inner_line = LineGraph(p1=center, length=150, angle=300)
        inner_line.draw(w=w, animation=True)
        circle = CircleGraph(center=inner_line.p2.coordinate, radius =150, color="#008000", thickness=2)
        circle.draw_circle(window=w)

        circle = CircleGraph(center=center.coordinate, radius =150, color="#008000", thickness=2)
        circle.draw_circle(window=w)
        w.mainloop()
        return False

    except Exception as e:
        print("Exception on main(): ", e)
        return True


draw()
