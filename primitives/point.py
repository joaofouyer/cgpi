# coding: utf-8
from primitives.coordinate import Coordinate


class Point:
    def __init__(self, coordinate=Coordinate()):
        try:
            x, y = coordinate.get_coordinate()
            self.x = x
            self.y = y

        except Exception as e:
            print("Exception in Point's init: ", e)

    @staticmethod
    def find_p2(origin, length, angle):
        try:
            from math import cos, sin, radians
            """"
            Given an origin, length and an angle, this method finds the destination point!
            :param origin: an origin point. Must be point type.
            :param length: the length of the line, in pixels (integer)
            :param angle: the angle from the origin from 0 to 360 degrees
            :return: p2c
            """
            x = round(origin.x + cos(radians(angle))*length)
            y = round(origin.y + sin(radians(angle))*length)
            coordinate = Coordinate(x=x, y=y)
            p2 = Point(coordinate=coordinate)
            return p2

        except Exception as e:
            print("Exception on find_p2: ", e)
            return False
