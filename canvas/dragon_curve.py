from .primitives.line_graph import LineGraph
from .primitives.point_graph import PointGraph
from .gui.window import Window

"""
Doesn't work yet. For Dragon Curve fully working please refer to dragon_curve_test that was implemented with turtle.
"""


class DragonCurve:
    window = Window(title="Curva do Dragão", width=1000, height=1000, background="#FFFFFF")
    origin = PointGraph(x=150, y=150)

    def dragon_curve(self, order, length, angle):
        try:
            if order:
                angle = (angle + 45) % 360
                self.dragon_curve(order=order-1, length=length, angle=angle)
                angle = (angle - 45) % 360
                self.dragon_curve(order=order-1, length=length, angle=angle)
                angle = (angle + 45) % 360
            else:
                line = LineGraph(p1=self.origin, length=length, angle=angle)
                line.draw(w=self.window, animation=True)
                self.origin = line.p2

            return False
        except Exception as e:
            print("Exception on dragon_curve: ", e)
            return True


d = DragonCurve()
d.dragon_curve(order=4, length=100, angle=0)
d.window.mainloop()
