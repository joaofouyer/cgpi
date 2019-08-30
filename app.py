# coding: utf-8

from gui.window import Window
from primitives import circle
from primitives.coordinate import Coordinate
from primitives.point_graph import PointGraph
from primitives.line_graph import LineGraph
from primitives.circle import Circle
from primitives.circle_graph import CircleGraph



def main():
    try:
        w = Window(title="Testando Pontos Animados", width=640, height=480, background="white")
        coordinate_p1 = Coordinate(x=100, y=100)
        p1 = PointGraph(window=w, coordinate=coordinate_p1)
        cc = CircleGraph(center=Coordinate(x=50, y=50), radius=50, color="#000000", thickness=2)
        cc.draw_circle(window=w)
        w.mainloop()
        return False

    except Exception as e:
        print("Exception on main(): ", e)
        return True
    
main()