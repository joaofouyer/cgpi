# coding: utf-8
from gui.window import Window
from primitives.circle_graph import CircleGraph
from primitives.line_graph import LineGraph
from primitives.point import Point
from structures.action import Action


def main():
    try:
        w = Window(title="Testando Desfazer Ações", width=700, height=650, background="white", actions=Action())
        cc = CircleGraph(center=Point(x=120, y=120), radius=50, color="#000000", thickness=2)
        cc.draw(window=w)
        line = LineGraph(p1=Point(x=200, y=300), p2=Point(x=500, y=100))
        line.draw(window=w)
        w.actions.undo(window=w)
        w.actions.undo(window=w)
        w.actions.redo(window=w)
        w.mainloop()
        return False

    except Exception as e:
        print("Exception on main(): ", e)
        return True


main()
