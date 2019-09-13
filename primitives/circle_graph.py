# coding: utf-8
from primitives.circle import Circle
from primitives.point_graph import PointGraph
from primitives.coordinate import Coordinate
from structures.action import Action
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
    
    def draw(self, window):
        try:
            for angle in range(0, 3600):
                xc = round(self.build_circle_x(angle))
                yc = round(self.build_circle_y(angle))
                coordinate_cc = Coordinate(x=xc, y=yc)
                pt = PointGraph(window=window, coordinate=coordinate_cc, size=self.thickness, color=self.color)
                pt.draw()
            window.actions.append(action=self)
        except Exception as e:
            print("Exception on draw_circle: ", e)
            return True
