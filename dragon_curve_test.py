# coding: utf-8
from turtle import right, left, forward, speed, exitonclick, hideturtle


class Dragon:
    speed(0)
    hideturtle()

    def dragon(self, order=4, length=200, angle=45):
        if order:
            right(angle)
            length = round(length / 1.41421356237)
            self.dragon(order - 1, length=length, angle=45)
            left(angle * 2)
            self.dragon(order - 1, length=length, angle=-45)
            right(angle)
        else:
            forward(length)


d = Dragon()
d.dragon(6)
exitonclick()
