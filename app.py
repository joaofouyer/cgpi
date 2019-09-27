# coding: utf-8
from gui.window import Window
from primitives.circle_graph import CircleGraph
from primitives.rectangle_graph import RectangleGraph
from primitives.line_graph import LineGraph
from primitives.point import Point
from structures.action import Action


def main():
    try:
        w = Window(title="Testando Desfazer Ações", width=700, height=650, background="white", actions=Action())
        rec = RectangleGraph(p1=Point(x=25, y=50), p2=Point(x=250, y=200), color="#000000", thickness=2)
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
