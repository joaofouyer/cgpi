# coding: utf-8
import sys
from primitives.line_graph import LineGraph


class PolygonGraph:
    def __init__(self, points=None, color="#000000", thickness=1):
        if sys.version_info[0] < 3:
            super(PolygonGraph, self).__init__()
        else:
            super().__init__()
        self.points = points
        self.color = color
        self.thickness = thickness

    def draw(self, window):
        try:
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
            # self.draw(window=window) TODO PEGAR OS PONTOS DA AÇÃO
            self.color = original_color
            return False
        except Exception as e:
            print("Exception on polygon.erase: ", e)
            return True

    def push(self, point):
        try:
            if self.points:
                self.points.append(point)
            else:
                self.points = []
                self.points.append(point)
            return False
        except Exception as e:
            print("Exception on polygon.append: ", e)