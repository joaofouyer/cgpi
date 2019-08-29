# coding: utf-8

from gui.window import Window
from primitives.coordinate import Coordinate
from primitives.point import Point
from primitives.line_graph import LineGraph


class App:
    @staticmethod
    def main():
        try:
            w = Window(title="Testando Pontos Animados", width=640, height=480, background="white")
            coordinate_p1 = Coordinate(x=50, y=50)
            p1 = Point(window=w, coordinate=coordinate_p1)
            coordinate_p2 = Coordinate(x=200, y=50)
            p2 = Point(window=w, coordinate=coordinate_p2)
            line = LineGraph(p1=p1, p2=p2, color="blue", thickness=2)
            line.draw(w=w, animation=False)

            w.mainloop()
            return False

        except Exception as e:
            print("Exception on main(): ", e)
            return True



app = App()
app.main()
