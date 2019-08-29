# coding: utf-8

from gui.window import Window
from primitives.coordinate import Coordinate
from primitives.point_graph import PointGraph
from primitives.line_graph import LineGraph


class App:
    @staticmethod
    def main():
        try:
            w = Window(title="Testando Pontos Animados", width=600, height=600, background="white")
            coordinate_p1 = Coordinate(x=300, y=300)
            p1 = PointGraph(coordinate=coordinate_p1, window=w)
            coordinate_p2 = p1.find_p2(length=200, angle=0).coordinate
            p2 = PointGraph(coordinate=coordinate_p2, window=w)
            line0 = LineGraph(p1=p1, p2=p2, color="black", thickness=2)
            line0.draw(w=w, animation=False)

            coordinate_p2 = p1.find_p2(length=200, angle=180).coordinate
            p2 = PointGraph(coordinate=coordinate_p2, window=w)
            line180 = LineGraph(p1=p1, p2=p2, color="blue", thickness=2)
            line180.draw(w=w, animation=False)

            coordinate_p2 = p1.find_p2(length=200, angle=90).coordinate
            p2 = PointGraph(coordinate=coordinate_p2, window=w)
            line90 = LineGraph(p1=p1, p2=p2, color="red", thickness=2)
            line90.draw(w=w, animation=False)

            coordinate_p2 = p1.find_p2(length=200, angle=270).coordinate
            p2 = PointGraph(coordinate=coordinate_p2, window=w)
            line270 = LineGraph(p1=p1, p2=p2, color="yellow", thickness=2)
            line270.draw(w=w, animation=False)

            coordinate_p2 = p1.find_p2(length=200, angle=45).coordinate
            p2 = PointGraph(coordinate=coordinate_p2, window=w)
            line45 = LineGraph(p1=p1, p2=p2, color="purple", thickness=2)
            line45.draw(w=w, animation=False)

            coordinate_p2 = p1.find_p2(length=200, angle=135).coordinate
            p2 = PointGraph(coordinate=coordinate_p2, window=w)
            line135 = LineGraph(p1=p1, p2=p2, color="green", thickness=2)
            line135.draw(w=w, animation=False)

            w.mainloop()
            return False

        except Exception as e:
            print("Exception on main(): ", e)
            return True



app = App()
app.main()
