# coding: utf-8

from gui.window import Window
from primitives.coordinate import Coordinate
from primitives.point_graph import PointGraph
from primitives.point import Point
from primitives.line_graph import LineGraph
from primitives.line import Line


class App:
    @staticmethod
    def main():
        try:
            w = Window(title="Retas", width=500, height=500, background="#FFFFFF")
            p1 = PointGraph(coordinate=Coordinate(x=50, y=250), window=w, size=2, color="#000000")
            p2 = PointGraph(coordinate=Coordinate(x=450, y=250), window=w, size=2, color="#000000")
            line = LineGraph(p1=p1, p2=p2)
            line.draw(w=w, animation=True)

            p1 = PointGraph(coordinate=Coordinate(x=250, y=50), window=w, size=2, color="#000000")
            line = LineGraph(p1=p1, length=400, angle=270)
            line.draw(w=w, animation=True)

            w.mainloop()
            return False

        except Exception as e:
            print("Exception on main(): ", e)
            return True


app = App().main()
