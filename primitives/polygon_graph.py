# coding: utf-8
import sys
from primitives.line_graph import LineGraph


class PolygonGraph:
    def __init__(self, points=None, color="#000000", thickness=1):
        super(PolygonGraph, self).__init__() if sys.version_info[0] < 3 else super().__init__()
        self.points = points if points else []
        self.color = color
        self.thickness = thickness

    def draw(self, window, multiple_points=True):
        try:
            if multiple_points:
                previous = self.points[-1]
                for p in self.points:
                    current = p
                    LineGraph(p1=previous, p2=current, color=self.color, thickness=self.thickness).draw(
                        window=window, action=False
                    )
                    previous = current
            else:
                p1, p2 = self.points[-2], self.points[-1]
                LineGraph(p1=p1, p2=p2, color=self.color, thickness=self.thickness).draw(window=window, action=False)
            window.refresh()
            return False
        except Exception as e:
            print("Exception on polygon.draw(): ", e)
            return True

    def erase(self, window):
        try:
            original_color = self.color
            self.color = window.background
            self.draw(window=window, multiple_points=True)
            self.color = original_color
            return False
        except Exception as e:
            print("Exception on polygon.erase: ", e)
            return True

    def push(self, point):
        try:
            self.points.append(point)
            return False
        except Exception as e:
            print("Exception on polygon.append: ", e)
