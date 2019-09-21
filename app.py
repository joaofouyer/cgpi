# coding: utf-8
from gui.window import Window
from primitives.circle_graph import CircleGraph
from primitives.rectangle_graph import RectangleGraph
from primitives.line_graph import LineGraph
from primitives.point import Point
from structures.action import Action
from gui.viewport import Viewport


def reduce_y(y):
    try:
        small_y = (y - 0) % (500 - 0)
        return (small_y - 0) % (150 - 0)
    except Exception as e:
        print("Failed to reduce y:", e)


def reduce_x(x):
    try:
        small_x = (x - 0) % (500 - 0)
        return (small_x - 0) % (150 - 0)
    except Exception as e:
        print("Failed to reduce x:", e)


def main():
    try:
        w = Window(title="Testando Desfazer Ações", width=700, height=650, background="white", actions=Action())
        vp = Viewport()
        rec = RectangleGraph(p1=Point(x=25, y=50), p2=Point(x=250, y=200), color="#000000", thickness=2)
        vp_rec = RectangleGraph(p1=Point(x=reduce_x(25), y=reduce_y(50)), p2=Point(x=reduce_x(250), y=reduce_y(200)), color="#000000", thickness=1)
        vp_rec.draw(window=vp)
        rec.draw(window=w)
        cc = CircleGraph(center=Point(x=120, y=120), radius=50, color="#000000", thickness=2)
        cc.draw(window=w)
        line = LineGraph(p1=Point(x=50, y=120), p2=Point(x=500, y=120))
        line.draw(window=w)
        w.mainloop()
        return False

    except Exception as e:
        print("Exception on main(): ", e)
        return True


main()
