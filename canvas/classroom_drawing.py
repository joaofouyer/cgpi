# coding: utf-8

from .gui.window import Window
from .primitives.point_graph import PointGraph
from .primitives.line_graph import LineGraph
from .primitives.circle_graph import CircleGraph


def draw():
    try:
        w = Window(title="Desenho da Sala", width=700, height=700, background="#FFFFFF")
        center = PointGraph(x=350, y=350, window=w, color="#000000")

        outer_lines = []
        for angle in [30, 90, 270, 150, 210, 330]:
            line = LineGraph(p1=center, length=260, angle=angle, color="#000000")
            line.draw(w=w)
            outer_lines.append(line)

        inner_lines = []
        angle = 0
        while angle < 360:
            line = LineGraph(p1=center, length=150, angle=angle, color="#ff0000")
            line.draw(w=w)
            inner_lines.append(line)
            angle = angle + 60

        circles = []
        for line in inner_lines:
            circle = CircleGraph(center=line.p2.coordinate, radius=150, color="#008000")
            circle.draw_circle(window=w)
            circles.append(circle)

        circle = CircleGraph(center=center.coordinate, radius=150, color="#008000")
        circle.draw_circle(window=w)

        for outer in outer_lines:
            for inner in outer_lines:
                outhex_line = LineGraph(p1=(outer).p2, p2=(inner).p2, color="#ff0000")
                outhex_line.draw(w=w)

        all_lines = outer_lines + inner_lines
        for line in all_lines:
            point = line.p2
            point.window = w
            point.color = "#0000FF"
            point.size = 5
            point.draw()

        w.mainloop()
        return False

    except Exception as e:
        print("Exception on main(): ", e)
        return True


draw()
