# coding: utf-8
from .circle import Circle
from .point_graph import PointGraph
import sys


class CircleGraph(Circle, object):
    def __init__(self, center, radius, color="#000000", thickness=1):
        try:
            if sys.version_info[0] < 3:
                super(CircleGraph, self).__init__(center, radius)
            else:
                super().__init__(center, radius)
            self.center = center
            self.radius = radius
            self.color = color 
            self.thickness = thickness
        except Exception as e:
            print("CircleGraph: ", e)
        
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
    
    def draw(self, window, action=True):
        try:
            for angle in range(0, 3600):
                x = round(self.build_circle_x(angle))
                y = round(self.build_circle_y(angle))
                PointGraph(window=window, x=x, y=y, size=self.thickness, color=self.color).draw()
            if action:
                window.actions.push(action=self)
            window.refresh()
            return False

        except Exception as e:
            print("Exception on draw_circle: ", e)
            return True

    def erase(self, window):
        try:
            original_color = self.color
            self.color = window.background
            self.draw(window=window, action=False)
            self.color = original_color
            return False
        except Exception as e:
            print("Exception on erase_circle: ", e)
            return True
