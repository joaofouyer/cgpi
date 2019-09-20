# coding: utf-8


class Point:
    def __init__(self, x, y):
        try:
            self.x = x
            self.y = y
            self.coordinate = self.x, self.y

        except Exception as e:
            print("Exception in Point's init: ", e)

    def get_coordinates(self):
        return self.x, self.y

    def find_p2(self, length, angle):
        try:
            from math import cos, sin, radians
            from primitives.point_graph import PointGraph
            """"
            Given an origin, length and an angle, this method finds the destination point!
            :param origin: an origin point. Must be point type.
            :param length: the length of the line, in pixels (integer)
            :param angle: the angle from the origin from 0 to 360 degrees
            :return: p2c
            """
            x = round(self.x + cos(radians(angle))*length)
            y = round(self.y + sin(radians(angle*-1))*length)

            p2 = PointGraph(x=x, y=y)
            return p2

        except Exception as e:
            print("Exception on find_p2: ", e)
            return False
