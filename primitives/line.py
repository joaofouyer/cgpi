# coding: utf-8


class Line:
    def __init__(self, p1, p2=None, length=None, angle=None):
        if p1:
            self.p1 = p1
        else:
            raise Exception("You must specify an origin point to draw a line!")
        if p2:
            self.p2 = p2
        elif length is not None and angle is not None:
            print(length, angle)
            self.p2 = p1.find_p2(length=length, angle=angle)
        else:
            raise Exception("To draw a line, you must specify p2 or its both length and angle from p1!")
        self.m = self.calc_slope()
        self.b = self.calc_b()

    def calc_slope(self):
        try:
            if self.p1.x == self.p2.x:
                return 0
            return (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)

        except Exception as e:
            print("Exception on calculate_slope: ", e)
            return False

    def calc_b(self):
        try:
            return self.p2.y - (self.m * self.p2.x)

        except Exception as e:
            print("Exception on calc_b: ", e)
            return False

    def delta_x_axis(self):
        try:
            return abs(self.p2.x - self.p1.x)
        except Exception as e:
            print("Exception on delta_y_axis: ", e)
            return False

    def delta_y_axis(self):
        try:
            return abs(self.p2.y - self.p1.y)
        except Exception as e:
            print("Exception on delta_y_axis: ", e)
            return False

    def x_linear_equation(self, y):
        try:
            return int((y - self.b) / self.m)
        except Exception as e:
            print("Exception on x_linear_equation: ", e)
            return False

    def y_linear_equation(self, x):
        try:
            return int(self.b + self.m * x)
        except Exception as e:
            print("Exception on x_linear_equation: ", e)
            return False
