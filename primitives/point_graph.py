# coding: utf-8
import sys
from primitives.point import Point
from primitives.coordinate import Coordinate


class PointGraph (Point, object):
    def __init__(self, coordinate=Coordinate(), window=None, size=1, color="#000000"):
        if sys.version_info[0] < 3:
            super(PointGraph, self).__init__(coordinate)
        else:
            super().__init__(coordinate)
        self.window = window
        self.size = size
        self.color = color

    def draw(self, append_action=False):
        try:
            if append_action:
                self.window.actions.append(self=self)
            self.window.canvas.create_oval(self.x-self.size, self.y-self.size, self.x + self.size, self.y + self.size, fill=self.color, outline=self.color)
            return False
        except Exception as e:
            print("Exception in Point.draw(): ", e)
            return True

    def valid_coordinate(self):
        try:
            if self.x < 0 or self.window.width < self.x:
                #    Adicionar tratamento quando o valor de x for inválido.
                return True
            if self.y < 0 or self.window.height < self.y:
                #    Adicionar tratamento quando o valor de y for inválido.
                return True
        except Exception as e:
            print("Exception in Point. ", e)
