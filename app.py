# coding: utf-8
from gui.window import Window
from primitives.circle_graph import CircleGraph
from primitives.rectangle_graph import RectangleGraph
from primitives.line_graph import LineGraph
from primitives.point import Point
from structures.action import Action


def main():
    try:
        w = Window(title="Testando Desfazer Ações", width=1500, height=700, background="white", actions=Action())
        w.mainloop()
        return False

    except Exception as e:
        print("Exception on main(): ", e)
        return True

main()
