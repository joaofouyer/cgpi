# coding: utf-8
import sys
from primitives.point_graph import PointGraph
from primitives.point import Point
from primitives.line import Line
from gui.animation import Animation


class LineGraph (Line, object):
    def __init__(self, p1, p2=None, length=None, angle=None, color="#000000", thickness=1):
        if sys.version_info[0] < 3:
            super(LineGraph, self).__init__(p1, p2, length, angle)
        else:
            super().__init__(p1, p2, length, angle)
        self.color = color
        self.thickness = thickness
        if isinstance(self.p1, Point):
            self.p1 = PointGraph(x=self.p1.x, y=self.p1.y, window=None, size=self.thickness, color=self.color)

        if isinstance(self.p2, Point):
            self.p2 = PointGraph(x=self.p2.x, y=self.p2.y, window=None, size=self.thickness, color=self.color)

    def set_properties(self, window, point):
        try:
            p = point
            p.color = self.color
            p.size = self.thickness
            p.window = window
            p.draw()
            return False
        except Exception as e:
            print("Exception on set_properties: ", e)
            return True

    def draw(self, window, animation=False, action=True):
        try:
            if action:
                window.actions.push(action=self)
            if self.delta_y_axis() > self.delta_x_axis():
                self.iterate_over_y_axis(window=window, animation=animation)
            else:
                self.iterate_over_x_axis(window=window, animation=animation)
            return False
        except Exception as e:
            print("Exception on line.draw(): ", e)
            return True

    def iterate_over_y_axis(self, window, animation=False):
        try:
            animation = Animation(window=window, speed=1) if animation else None
            if self.p1.y > self.p2.y:
                pivot, greater = self.p2, self.p1
            else:
                pivot, greater = self.p1, self.p2

            if pivot.x == greater.x:
                x = pivot.x
                self.set_properties(window=window, point=greater)
                for y in range(pivot.y, greater.y):
                    p = PointGraph(window=window, x=x, y=y, size=self.thickness, color=self.color)
                    animation.append_frame(frame=p) if animation else p.draw()
            else:
                self.set_properties(window=window, point=pivot)
                for y in range(pivot.y, greater.y):
                    x = self.x_linear_equation(y=y)
                    p = PointGraph(window=window, x=x, y=y, size=self.thickness, color=self.color)
                    animation.append_frame(frame=p) if animation else p.draw()
            animation.animate() if animation else False
            return False
        except Exception as e:
            print("Exception on iterate over y axis: ", e)
            return True

    def iterate_over_x_axis(self, window, animation=False):
        try:
            animation = Animation(window=window, speed=1) if animation else None
            if self.p1.x > self.p2.x:
                pivot, greater = self.p2, self.p1
            else:
                pivot, greater = self.p1, self.p2

            self.set_properties(window=window, point=pivot)
            for x in range(pivot.x, greater.x):
                y = self.y_linear_equation(x=x)
                p = PointGraph(window=window, x=x, y=y, size=self.thickness, color=self.color)
                animation.append_frame(frame=p) if animation else p.draw()
            animation.animate() if animation else False
            return False
        except Exception as e:
            print("Exception on iterate_over_x_axis: ", e)
            return True

    def erase(self, window):
        try:
            original_color = self.color
            self.color = window.background
            self.draw(window=window, animation=False, action=False)
            self.color = original_color
            return False
        except Exception as e:
            print("Exception on line_graph.erase: ", e)
            return True
