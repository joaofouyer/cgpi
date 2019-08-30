from primitives.line_graph import LineGraph
from primitives.point_graph import PointGraph
from primitives.coordinate import Coordinate
from gui.window import Window


class DragonCurve:
    window = Window(title="Curva do Dragão", width=1000, height=1000, background="#FFFFFF")

    def dragon_curve(self, order, length):
        try:
            p1 = PointGraph(coordinate=Coordinate(x=50, y=50))
            self.dragon_curve_recursive(order=order, length=length, angle=0, p1=p1)
            self.window.mainloop()
            return False
        except Exception as e:
            print("Exception on dragon_curve: ", e)
            return True

    def dragon_curve_recursive(self, order, length, angle, p1):
        try:
            if order:
                line = LineGraph(p1=p1, length=length, angle=angle)
                p1 = line.p2
                p1 = self.dragon_curve_recursive(order=order - 1, length=length, angle=angle, p1=p1)
                angle = (angle - 90) % 360
                p1 = self.dragon_curve_recursive(order=order - 1, length=length, angle=angle, p1=p1)
                return p1
            else:
                print("ang: ", angle, "origin: ", p1.x, p1.y)
                line = LineGraph(p1=p1, length=length, angle=angle)
                line.draw(w=self.window, animation=True)
                return line.p2
        except Exception as e:
            print("Exception on dragon_curve_recursive: ", e)


d = DragonCurve().dragon_curve(order=3, length=100)
