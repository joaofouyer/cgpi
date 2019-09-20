# coding: utf-8
import sys
from primitives.point_graph import PointGraph
from primitives.point import Point
from primitives.line_graph import LineGraph
from gui.animation import Animation


class RectangleGraph (LineGraph, object):
    def __init__(self, p1, p2, length=None, color="#000000", thickness=1):
        if sys.version_info[0] < 3:
            super(RectangleGraph, self).__init__(p1, p2, length)
        else:
            super().__init__(p1, p2, length)

        self.color = color
        self.thickness = thickness

        if isinstance(self.p1, Point):
            self.p1 = PointGraph(x=self.p1.x, y=self.p1.y, window=None, size=self.thickness, color=self.color)

        if isinstance(self.p2, Point):
            self.p2 = PointGraph(x=self.p2.x, y=self.p2.y, window=None, size=self.thickness, color=self.color)

        self.p3 = PointGraph(x=self.p1.x, y=self.p2.y, size=self.thickness, color=self.color)
        self.p4 = PointGraph(x=p2.x, y=p1.y, size=self.thickness, color=self.color)

    def draw(self, window, animation=False, action=True):
        try:
            if action:
                window.actions.push(action=self)
            LineGraph(self.p1, self.p3, color=self.color, thickness=self.thickness).draw(window=window, action=False)
            LineGraph(self.p3, self.p2, color=self.color, thickness=self.thickness).draw(window=window, action=False)
            LineGraph(self.p2, self.p4, color=self.color, thickness=self.thickness).draw(window=window, action=False)
            LineGraph(self.p4, self.p1, color=self.color, thickness=self.thickness).draw(window=window, action=False)

            window.refresh()
            return False
        except Exception as e:
            print("Exception on rectangle.draw(): ", e)
            return True

    def erase(self, window):
        try:
            original_color = self.color
            self.color = window.background
            self.draw(window=window, animation=False, action=False)
            self.color = original_color
            return False
        except Exception as e:
            print("Exception on rectangle_graph.erase: ", e)
            return True
