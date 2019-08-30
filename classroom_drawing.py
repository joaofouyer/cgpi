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
        center = PointGraph(coordinate=Coordinate(x=350, y=350), window=w, color="#000000")
        outer_line1 = LineGraph(p1=center, length=260, angle=270, color="#000000")
        outer_line1.draw(w=w)
        inner_line1 = LineGraph(p1=center, length=150, angle=0, color="#ff0000")
        inner_line1.draw(w=w)
        circle = CircleGraph(center=inner_line1.p2.coordinate, radius =150, color="#008000")
        circle.draw_circle(window=w)

        outer_line2= LineGraph(p1=center, length=260, angle=90, color="#ff1234")
        outer_line2.draw(w=w)
        inner_line2 = LineGraph(p1=center, length=150, angle=60, color="#ff0000")
        inner_line2.draw(w=w)
        circle = CircleGraph(center=inner_line2.p2.coordinate, radius =150, color="#008000")
        circle.draw_circle(window=w)

        outer_line3 = LineGraph(p1=center, length=260, angle=30)
        outer_line3.draw(w=w)
        inner_line3 = LineGraph(p1=center, length=150, angle=120, color="#ff0000")
        inner_line3.draw(w=w)
        circle = CircleGraph(center=inner_line3.p2.coordinate, radius =150, color="#008000")
        circle.draw_circle(window=w)

        outer_line4 = LineGraph(p1=center, length=260, angle=150)
        outer_line4.draw(w=w)

        inner_line4 = LineGraph(p1=center, length=150, angle=180, color="#ff0000")
        inner_line4.draw(w=w)
        circle = CircleGraph(center=inner_line4.p2.coordinate, radius =150, color="#008000")
        circle.draw_circle(window=w)

        outer_line5 = LineGraph(p1=center, length=260, angle=210)
        outer_line5.draw(w=w)

        inner_line5 = LineGraph(p1=center, length=150, angle=240, color="#ff0000")
        inner_line5.draw(w=w)
        circle = CircleGraph(center=inner_line5.p2.coordinate, radius =150, color="#008000")
        circle.draw_circle(window=w)

        outer_line6 = LineGraph(p1=center, length=260, angle=330)
        outer_line6.draw(w=w)

        inner_line6 = LineGraph(p1=center, length=150, angle=300, color="#ff0000")
        inner_line6.draw(w=w)
        circle = CircleGraph(center=inner_line6.p2.coordinate, radius =150, color="#008000")
        circle.draw_circle(window=w)

        circle = CircleGraph(center=center.coordinate, radius =150, color="#008000")
        circle.draw_circle(window=w)

        List = [outer_line1, outer_line2, outer_line3, outer_line4, outer_line5, outer_line6]
        List1 = [inner_line1, inner_line2, inner_line3, inner_line4, inner_line5, inner_line6]
        List2 = List + List1
        for x in List:
            for y in List:
                outhex_line = LineGraph(p1=(x).p2, p2=(y).p2, color="#ff0000")
                outhex_line.draw(w=w)
        
         
        for x in List2:
            x.p2.color = "#0000ff"
            x.p2.size = 5
            x.p2.draw()

        w.mainloop()
        return False

    except Exception as e:
        print("Exception on main(): ", e)
        return True


draw()
