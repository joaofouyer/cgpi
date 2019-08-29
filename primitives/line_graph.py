# coding: utf-8
import sys
from primitives.coordinate import Coordinate
from primitives.point_graph import PointGraph
from primitives.line import Line
from gui.animation import Animation


class LineGraph (Line, object):
    def __init__(self, p1, p2, color, thickness):
        if sys.version_info[0] < 3:
            super(LineGraph, self).__init__(p1, p2)
        else:
            super().__init__(p1, p2)

        self.color = color
        self.thickness = thickness

    def set_properties(self, window, point):
        try:
            p = point
            p.color = self.color
            p.size = self.thickness
            p.window = window
            p.draw()
        except Exception as e:
            print("Exception on set_properties: ", e)
            return True

    def draw(self, w, animation=False):
        try:
            if self.delta_y_axis() > self.delta_x_axis():
                self.iterate_over_y_axis(w, animation=animation)
            else:
                self.iterate_over_x_axis(w, animation=animation)

        except Exception as e:
            print("Exception on line.draw(): ", e)

    def iterate_over_y_axis(self, window, animation=False):
        try:
            animation = Animation(window=window, speed=5) if animation else None
            if self.p1.y > self.p2.y:
                pivot, greater = self.p2, self.p1
            else:
                pivot, greater = self.p1, self.p2

            if pivot.x == greater.x:
                x = pivot.x
                self.set_properties(window=window, point=greater)
                for y in range(pivot.y, greater.y):
                    c = Coordinate(x=x, y=y)
                    p = PointGraph(window=window, coordinate=c, size=self.thickness, color=self.color)
                    animation.append_frame(frame=p) if animation else p.draw()
            else:
                self.set_properties(window=window, point=pivot)
                for y in range(pivot.y, greater.y):
                    c = Coordinate(x=self.x_linear_equation(y=y), y=y)
                    p = PointGraph(window=window, coordinate=c, size=self.thickness, color=self.color)
                    animation.append_frame(frame=p) if animation else p.draw()
            animation.animate() if animation else False
            return False
        except Exception as e:
            print("Exception on iterate over y axis: ", e)
            return True

    def iterate_over_x_axis(self, window, animation=False):
        try:
            animation = Animation(window=window, speed=5) if animation else None
            if self.p1.x > self.p2.x:
                pivot, greater = self.p2, self.p1
            else:
                pivot, greater = self.p1, self.p2

            self.set_properties(window=window, point=pivot)
            for x in range(pivot.x, greater.x):
                c = Coordinate(x=x, y=self.y_linear_equation(x=x))
                p = PointGraph(window=window, coordinate=c, size=self.thickness, color=self.color)
                animation.append_frame(frame=p) if animation else p.draw()
            animation.animate() if animation else False
            return False
        except Exception as e:
            print("Exception on iterate_over_x_axis: ", e)
            return True
