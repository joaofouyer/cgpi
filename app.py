# coding: utf-8

from gui.window import Window
from primitives import circle
from primitives.coordinate import Coordinate
from primitives.point import Point
from primitives.line_graph import LineGraph
from primitives.circle import Circle
from primitives.circle_graph import CircleGraph


class App:
    
    @staticmethod
    def menhe():
        try:
            w = Window(title="Testando Pontos Animados", width=640, height=480, background="white")
            coordinate_p1 = Coordinate(x=100, y=100)
            p1 = Point(window=w, coordinate=coordinate_p1)
            cc = CircleGraph(coordinate_p1, 250, "#000000", 2)
            cc.drawCircle(w)
            w.mainloop()
            return False

        except Exception as e:
            print("Exception on main(): ", e)
            return True
    
    

app = App()
app.menhe()