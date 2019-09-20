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
            p3 = PointGraph(p1.y, p2.x, w=window, size=1, color=#000000)
            p4 = PointGraph(p1.x, p2.y, w=window, size=1, color=  # 000000)
            line1 = LineGraph(p1, p3, color="#000000", thickness=1)
            line2 = LineGraph(p2, p4, color="#000000", thickness=1)
            line3 = LineGraph(p1, p4, color="#000000", thickness=1)
            line4 = LineGraph(p2, p3, color="#000000", thickness=1)
            window.refresh()
            return False
        except Exception as e:
            print("Exception on line.draw(): ", e)
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
