# coding: utf-8
import sys
from .point import Point


class PointGraph (Point, object):
    def __init__(self, x, y, window=None, size=1, color="#000000"):
        if sys.version_info[0] < 3:
            super(PointGraph, self).__init__(x=x, y=y)
        else:
            super().__init__(x=x, y=y)
        self.window = window
        self.size = size
        self.color = color

    def draw(self, window=None, append_action=False):
        try:
            if append_action:
                self.window.actions.push(self=self)

            if self.window.clipping:
                if self.window.clipping.min_x < self.x < self.window.clipping.max_x and \
                        self.window.clipping.min_y < self.y < self.window.clipping.max_y:
                    x = self.x - self.window.clipping.left_margin
                    y = self.y - self.window.clipping.top_margin
                    self.window.clipping.canvas.create_oval(
                        x - self.size,
                        y - self.size,
                        x,
                        y,
                        fill=self.color,
                        outline=self.color
                    )

            self.window.canvas.create_oval(
                self.x-self.size,
                self.y-self.size,
                self.x,
                self.y,
                fill=self.color,
                outline=self.color
            )

            vp_x, vp_y = self.window.viewport.reduce(x=self.x, y=self.y, window=self.window)

            self.window.viewport.canvas.create_oval(
                vp_x - 1, vp_y - 1, vp_x, vp_y, fill=self.color,
                outline=self.color
            )

            if window:
                window.refresh()
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

    def erase(self, window):
        try:
            original_color = self.color
            self.color = window.background
            self.draw(append_action=False)
            self.color = original_color
            return False
        except Exception as e:
            print("Exception on PointGraph.erase: ", e)
            return True
