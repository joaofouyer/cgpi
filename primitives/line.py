# coding: utf-8


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
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
